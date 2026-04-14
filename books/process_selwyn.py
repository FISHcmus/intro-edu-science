"""
Process "Distrusting Educational Technology" by Neil Selwyn (2014, Routledge)
from PDF into clean organized markdown, using font-size analysis for headings.

Chapter map (1-based page numbers from PDF):
- p1-2:   Cover / Archive notice
- p3:     Back cover blurb
- p5:     Title page
- p6:     Copyright page
- p7:     Contents
- p9-11:  Preface
- p13-14: Acknowledgements
- p15-33: Chapter 1 — Why Distrust Educational Technology?
- p34-55: Chapter 2 — Understanding Educational Technology as Ideology
- p56-77: Chapter 3 — Distrusting 'Virtual' Technologies in Education
- p78-97: Chapter 4 — Distrusting 'Open' Technologies in Education
- p98-118: Chapter 5 — Distrusting 'Games' Technologies in Education
- p119-138: Chapter 6 — Distrusting 'Social' Technologies in Education
- p139-157: Chapter 7 — Educational Technology: Continuities, Contradictions and Conflicts
- p158-180: Chapter 8 — Educational Technology: Is There an Alternative?
- p181-202: References
- p203-214: Index

Font size thresholds (observed):
- Chapter title:    17+ pt  → ## heading (skip, already set at section level)
- Section heading:  9.4+    → ### heading
- Body text:        ~7-8.8 pt
- Running header:   ~7.2 pt (same as body but matches known strings)
"""

import fitz
import re
import sys

PDF_PATH = "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Distrusting Educational Technology - Selwyn.pdf"
OUT_PATH = "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Distrusting Educational Technology - Selwyn.md"

# Running headers to suppress (these appear at top of each page)
RUNNING_HEADER_PATTERNS = [
    r"^Why Distrust Educational Technology\?$",
    r"^Understanding Educational Technology as Ideology$",
    r"^Distrusting\s+'?Virtual'?\s+Technologies in Education$",
    r"^Distrusting\s+'?Open'?\s+Technologies in Education$",
    r"^Distrusting\s+'?Games'?\s+Technologies in Education$",
    r"^Distrusting\s+'?Social'?\s+Technologies in Education$",
    r"^Educational Technology:\s*Continuities,\s*Contradictions and Conflicts$",
    r"^Educational Technology:\s*Is There an Alternative\?$",
    r"^Preface$",
    r"^Acknowledgements$",
    r"^References$",
    r"^Index$",
    # Chapter 7 and 8 subtitles (appear at heading size on chapter start page)
    r"^Continuities,\s*Contradictions and Conflicts$",
    r"^Is\s+There\s+an\s+Alternative\?$",
]
RUNNING_HEADER_RE = re.compile(
    '|'.join(RUNNING_HEADER_PATTERNS),
    re.IGNORECASE,
)

# Chapter title markers to skip (large font, already used as ## level headings)
CHAPTER_TITLE_THRESHOLD = 14.0
# Section heading threshold
SECTION_HEADING_THRESHOLD = 9.0
# Body text max size
BODY_MAX = 9.3


def is_garbled_page(raw_text: str) -> bool:
    """Return True if the page appears to be a scanned image with no real text."""
    stripped = raw_text.strip()
    if not stripped:
        return True
    alpha_count = sum(1 for c in stripped if c.isalpha())
    if alpha_count < 50:
        return True
    # Check ratio: if alpha chars are < 30% of total non-space chars, likely OCR garble
    non_space = sum(1 for c in stripped if not c.isspace())
    if non_space > 0 and alpha_count / non_space < 0.35:
        return True
    # Check word count — real prose pages have many short words
    words = stripped.split()
    avg_word_len = sum(len(w) for w in words) / max(len(words), 1)
    # Garbled OCR tends to have very long "words" (random character clusters)
    if avg_word_len > 12 and len(words) < 100:
        return True
    return False


def normalize_spaces(text: str) -> str:
    """Collapse multiple spaces into one (artifact from PDF extraction)."""
    return re.sub(r'  +', ' ', text)


def classify_line(line_text: str, avg_size: float) -> str:
    """Classify a single line as 'skip', 'heading', or 'body'."""
    if not line_text:
        return 'skip'

    if avg_size >= CHAPTER_TITLE_THRESHOLD:
        return 'skip'

    if avg_size >= SECTION_HEADING_THRESHOLD:
        # Running header → skip
        if RUNNING_HEADER_RE.match(line_text):
            return 'skip'
        # False positive: ends with sentence-terminal punctuation
        if line_text.rstrip()[-1] in '.,);:':
            return 'body'
        # False positive: starts with lowercase (mid-sentence fragment)
        if line_text[0].islower():
            return 'body'
        # False positive: single word that isn't a known standalone heading
        known_single = {'Introduction', 'Conclusions', 'Preface', 'Acknowledgements',
                        'References', 'Index', 'introduction', 'conclusions'}
        if len(line_text.split()) == 1 and line_text not in known_single:
            return 'body'
        # False positive: ≤3 words starting with common article/preposition (body fragment)
        words = line_text.split()
        short_starters = {'An', 'A', 'The', 'To', 'As', 'In', 'Of', 'For', 'By', 'On', 'At', 'With', 'From'}
        if len(words) <= 3 and words[0] in short_starters:
            return 'body'
        return 'heading'

    # Body size
    if re.match(r'^\s*[\dxivXIV]+\s*$', line_text):
        return 'skip'
    if RUNNING_HEADER_RE.match(line_text):
        return 'skip'
    return 'body'


def extract_page_elements(page) -> list[dict]:
    """
    Extract text elements from a page with font-size tags.
    Returns list of dicts: {'type': 'heading'|'body'|'skip', 'text': str}

    Multi-line headings in the same PDF block are merged into one heading element.
    """
    raw = page.get_text()
    if is_garbled_page(raw):
        return []

    elements = []
    data = page.get_text('dict')

    for block in data.get('blocks', []):
        if 'lines' not in block:
            continue

        # Collect all lines in this block with their classifications
        block_line_data = []
        for line in block['lines']:
            spans = [s for s in line['spans'] if s['text'].strip()]
            if not spans:
                continue
            line_text = normalize_spaces(' '.join(s['text'] for s in spans).strip())
            if not line_text:
                continue
            sizes = [s['size'] for s in spans]
            avg_size = sum(sizes) / len(sizes)
            # Skip lines that are only punctuation/separator chars (e.g., '|', '—', decorators)
            if re.match(r'^[|—\-_=\s]+$', line_text):
                block_line_data.append({'type': 'skip', 'text': line_text, 'size': avg_size})
                continue
            classification = classify_line(line_text, avg_size)
            block_line_data.append({'type': classification, 'text': line_text, 'size': avg_size})

        if not block_line_data:
            continue

        # If all non-skip lines in this block are headings, merge them into one heading
        non_skip = [d for d in block_line_data if d['type'] != 'skip']
        if non_skip and all(d['type'] == 'heading' for d in non_skip):
            merged_text = ' '.join(d['text'] for d in non_skip)
            elements.append({'type': 'heading', 'text': merged_text, 'size': non_skip[0]['size']})
        else:
            # Mixed block or all body — emit each line individually
            elements.extend(block_line_data)

    return elements


def join_body_lines(elements: list[dict]) -> list[dict]:
    """
    Join consecutive body text lines into paragraphs.
    A new paragraph starts when:
    - There was a heading in between
    - The previous line ends with a sentence-ending punctuation and the
      current line starts with a capital letter (rough heuristic)
    - Or we just accumulate all body lines and split by blank elements.

    Simple approach: accumulate body lines, yield paragraph when heading seen.
    """
    result = []
    current_body_lines = []

    def flush_body():
        if current_body_lines:
            # Fix hyphenation within accumulated lines before joining
            # Join lines, fixing hyphenation at line boundaries
            joined_lines = []
            for i, ln in enumerate(current_body_lines):
                if ln.endswith('-') and i < len(current_body_lines) - 1:
                    # Soft hyphen: merge with next
                    joined_lines.append(ln[:-1])
                else:
                    joined_lines.append(ln + ' ')
            text = ''.join(joined_lines).strip()
            # Fix remaining "word- word" artifacts
            text = re.sub(r'(\w)- ([a-z])', r'\1\2', text)
            # Split into paragraphs: when a line starts with capital after a sentence end
            # Use a simple paragraph-boundary heuristic
            paragraphs = split_into_paragraphs(current_body_lines)
            for p in paragraphs:
                if p:
                    result.append({'type': 'body', 'text': p})
            current_body_lines.clear()

    for elem in elements:
        if elem['type'] == 'skip':
            continue
        elif elem['type'] == 'heading':
            # Block-level merging already handled multi-line headings in extract_page_elements
            flush_body()
            result.append({'type': 'heading', 'text': elem['text']})
        else:  # body
            current_body_lines.append(elem['text'])

    flush_body()
    return result


def split_into_paragraphs(lines: list[str]) -> list[str]:
    """
    Given a list of body text lines from PDF extraction,
    group them into paragraphs.

    Heuristics for paragraph break:
    - A line that ends with period/question mark/exclamation followed by
      a line that starts with a capital letter and the current accumulated
      text is >= 40 chars (not a short fragment).
    """
    if not lines:
        return []

    paragraphs = []
    # Build text incrementally, tracking soft-hyphen state
    current_text = ''
    prev_soft_hyphen = False  # was the previous line a soft-hyphen line?

    def flush_paragraph():
        nonlocal current_text
        text = current_text.strip()
        text = re.sub(r'  +', ' ', text)
        if text:
            paragraphs.append(text)
        current_text = ''

    for line in lines:
        stripped_line = line.rstrip()
        if not stripped_line:
            continue

        if stripped_line.endswith('-'):
            # Soft-hyphen line: strip hyphen, concatenate with next directly
            word_part = stripped_line[:-1]
            if prev_soft_hyphen:
                # Previous also was soft-hyphen, concatenate directly
                current_text += word_part
            elif current_text:
                current_text += ' ' + word_part
            else:
                current_text = word_part
            prev_soft_hyphen = True
        else:
            if prev_soft_hyphen:
                # Previous was soft-hyphen: concatenate without space
                current_text += stripped_line
            elif current_text:
                current_text += ' ' + stripped_line
            else:
                current_text = stripped_line
            prev_soft_hyphen = False

            # Check if we should break paragraph here
            combined = re.sub(r'  +', ' ', current_text)
            if (stripped_line.rstrip().endswith(('.', '!', '?', ')"', '."', "\u2019", '.'))
                    and len(combined) >= 60):
                paragraphs.append(combined.strip())
                current_text = ''
                prev_soft_hyphen = False

    # Flush remainder
    if current_text.strip():
        combined = re.sub(r'  +', ' ', current_text)
        paragraphs.append(combined.strip())

    return [p for p in paragraphs if p]


def process_pages(doc, start_page: int, end_page: int) -> str:
    """
    Process pages start_page..end_page (1-based, inclusive) into markdown body.
    Returns formatted markdown string.
    """
    all_elements = []
    for pg_num in range(start_page, end_page + 1):
        page = doc[pg_num - 1]
        elements = extract_page_elements(page)
        all_elements.extend(elements)

    # Join consecutive body lines into paragraphs, keep headings
    joined = join_body_lines(all_elements)

    # Build markdown
    md_parts = []
    for elem in joined:
        if elem['type'] == 'heading':
            md_parts.append(f'### {elem["text"]}')
        else:
            md_parts.append(elem['text'])

    return '\n\n'.join(md_parts)


def build_full_markdown(doc) -> str:
    sections = []

    # Title block
    sections.append(
        "# Distrusting Educational Technology: Critical Questions for Changing Times\n\n"
        "**Neil Selwyn**  \n"
        "*Monash University, Australia*  \n"
        "*Routledge, New York and London, 2014*\n\n"
        "---"
    )

    # Preface
    preface_body = process_pages(doc, 9, 11)
    sections.append("## Preface\n\n" + preface_body)

    # Acknowledgements
    ack_body = process_pages(doc, 13, 14)
    sections.append("## Acknowledgements\n\n" + ack_body)

    # Chapter 1
    ch1_body = process_pages(doc, 15, 33)
    sections.append("## Chapter 1: Why Distrust Educational Technology?\n\n" + ch1_body)

    # Chapter 2
    ch2_body = process_pages(doc, 34, 55)
    sections.append("## Chapter 2: Understanding Educational Technology as Ideology\n\n" + ch2_body)

    # Chapter 3
    ch3_body = process_pages(doc, 56, 77)
    sections.append("## Chapter 3: Distrusting 'Virtual' Technologies in Education\n\n" + ch3_body)

    # Chapter 4
    ch4_body = process_pages(doc, 78, 97)
    sections.append("## Chapter 4: Distrusting 'Open' Technologies in Education\n\n" + ch4_body)

    # Chapter 5
    ch5_body = process_pages(doc, 98, 118)
    sections.append("## Chapter 5: Distrusting 'Games' Technologies in Education\n\n" + ch5_body)

    # Chapter 6
    ch6_body = process_pages(doc, 119, 138)
    sections.append("## Chapter 6: Distrusting 'Social' Technologies in Education\n\n" + ch6_body)

    # Chapter 7
    ch7_body = process_pages(doc, 139, 157)
    sections.append(
        "## Chapter 7: Educational Technology: Continuities, Contradictions and Conflicts\n\n"
        + ch7_body
    )

    # Chapter 8 (p158-179; p180 is garbled scan)
    ch8_body = process_pages(doc, 158, 179)
    sections.append("## Chapter 8: Educational Technology: Is There an Alternative?\n\n" + ch8_body)

    # References (p181-201; p202 is garbled)
    refs_body = process_pages(doc, 181, 201)
    sections.append("## References\n\n" + refs_body)

    # Index (p203-205; p206+ is back matter/promo)
    idx_body = process_pages(doc, 203, 205)
    sections.append("## Index\n\n" + idx_body)

    return '\n\n---\n\n'.join(sections)


def final_cleanup(md: str) -> str:
    """Final cleanup passes on the complete markdown."""
    # Remove multiple consecutive blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    # Clean trailing spaces
    md = re.sub(r' +\n', '\n', md)
    # Fix "word-  word" and "word- word" hyphenation artifacts (soft hyphens with trailing space)
    md = re.sub(r'(\w)-\s+([a-z])', r'\1\2', md)
    # Fix OCR artifact "and.the" → "and the"
    md = md.replace('and.the', 'and the')
    # Remove lines that are only whitespace
    md = re.sub(r'(?m)^ +$', '', md)
    # Final blank line collapse
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


def main():
    print("Opening PDF...", file=sys.stderr)
    doc = fitz.open(PDF_PATH)
    print(f"Pages: {doc.page_count}", file=sys.stderr)

    print("Processing pages with font-size heading detection...", file=sys.stderr)
    md = build_full_markdown(doc)

    print("Running final cleanup...", file=sys.stderr)
    md = final_cleanup(md)

    print(f"Writing to {OUT_PATH}...", file=sys.stderr)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        f.write(md)

    char_count = len(md)
    word_count = len(md.split())
    heading_count = len(re.findall(r'^#{1,4} ', md, re.MULTILINE))
    print(f"Done: {char_count:,} chars, {word_count:,} words, {heading_count} headings.", file=sys.stderr)


if __name__ == '__main__':
    main()
