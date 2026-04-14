#!/usr/bin/env python3
"""
Extract 3 EPUB books to markdown format.

EPUBs are ZIP files. Extract, parse TOC, read HTML chapters, convert to markdown.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Tuple
import html
import sys

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: beautifulsoup4 not installed. Install with: pip install beautifulsoup4 lxml")
    sys.exit(1)

# EPUB books to extract
BOOKS = [
    {
        "epub": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Plagiarism in Higher Education - Eaton.epub",
        "output": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Plagiarism in Higher Education - Eaton.md",
        "title": "Plagiarism in Higher Education - Eaton"
    },
    {
        "epub": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Should Robots Replace Teachers - Selwyn.epub",
        "output": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Should Robots Replace Teachers - Selwyn.md",
        "title": "Should Robots Replace Teachers - Selwyn"
    },
    {
        "epub": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Machine Learning and Human Intelligence - Luckin.epub",
        "output": "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/books/Machine Learning and Human Intelligence - Luckin.md",
        "title": "Machine Learning and Human Intelligence - Luckin"
    }
]


def find_opf_file(zip_file) -> str:
    """Find OPF file (content.opf or volume.opf)."""
    for name in zip_file.namelist():
        if 'opf' in name.lower() and name.endswith('.opf'):
            return name
    return None


def get_toc_from_opf(zip_file, opf_path: str) -> List[Tuple[str, str]]:
    """
    Parse OPF file to get chapter files and order.
    Returns list of (filename, title) tuples.
    """
    try:
        opf_content = zip_file.read(opf_path).decode('utf-8')
        root = ET.fromstring(opf_content)

        # Parse namespaces
        ns = {
            'opf': 'http://www.idpf.org/2007/opf',
            'spine': 'http://www.idpf.org/2007/opf'
        }

        # Try to get manifest and spine
        manifest = {}
        for item in root.findall('.//opf:manifest/opf:item', ns):
            item_id = item.get('id')
            href = item.get('href')
            if href:
                manifest[item_id] = href

        chapters = []
        for itemref in root.findall('.//opf:spine/opf:itemref', ns):
            idref = itemref.get('idref')
            if idref and idref in manifest:
                href = manifest[idref]
                # Extract filename without path
                filename = href.split('/')[-1]
                chapters.append((href, filename))

        return chapters
    except Exception as e:
        print(f"  Warning: Could not parse OPF: {e}")
        return []


def find_toc_ncx(zip_file) -> str:
    """Find and return path to toc.ncx if it exists."""
    for name in zip_file.namelist():
        if name.endswith('toc.ncx'):
            return name
    return None


def html_to_markdown(html_content: str) -> str:
    """
    Convert HTML to markdown using BeautifulSoup.
    Handles basic tags: h1-h3, p, ul, ol, blockquote, code, etc.
    """
    try:
        soup = BeautifulSoup(html_content, 'lxml')
    except:
        soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, and metadata tags
    for tag in soup(['script', 'style', 'nav', 'meta', 'link']):
        tag.decompose()

    markdown = []

    for element in soup.body.descendants if soup.body else soup.descendants:
        if isinstance(element, str):
            text = str(element).strip()
            if text and text not in ['\n', '\r\n', ' ']:
                markdown.append(text)
        elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text:
                markdown.append(f"{'#' * level} {text}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                markdown.append(f"{text}\n")
        elif element.name in ['ul', 'ol']:
            for li in element.find_all('li', recursive=False):
                li_text = li.get_text(strip=True)
                if li_text:
                    if element.name == 'ul':
                        markdown.append(f"- {li_text}\n")
                    else:
                        markdown.append(f"1. {li_text}\n")
        elif element.name == 'blockquote':
            text = element.get_text(strip=True)
            if text:
                markdown.append(f"> {text}\n")
        elif element.name == 'code':
            text = element.get_text(strip=True)
            if text:
                markdown.append(f"`{text}`")

    # Join and clean up
    result = '\n'.join(markdown)
    # Remove excessive blank lines
    result = re.sub(r'\n\n\n+', '\n\n', result)
    return result


def extract_epub(epub_path: str, output_path: str, title: str):
    """Extract EPUB to markdown."""
    print(f"\nExtracting: {title}")
    print(f"  Source: {epub_path}")

    if not os.path.exists(epub_path):
        print(f"  ERROR: File not found")
        return False

    try:
        with zipfile.ZipFile(epub_path, 'r') as zip_file:
            # List all files for debugging
            all_files = zip_file.namelist()

            # Find OPF file
            opf_path = find_opf_file(zip_file)

            if not opf_path:
                print(f"  ERROR: OPF file not found")
                return False

            print(f"  Found: {opf_path}")

            # Get chapter order from OPF
            chapters = get_toc_from_opf(zip_file, opf_path)
            if not chapters:
                print(f"  ERROR: Could not parse chapters from OPF")
                return False
            print(f"  Found {len(chapters)} chapters")

            # Extract and convert chapters
            markdown_content = f"# {title}\n\n"

            base_dir = os.path.dirname(opf_path)

            for href, filename in chapters:
                # Resolve relative paths
                if href.startswith('../'):
                    full_path = os.path.normpath(os.path.join(base_dir, href))
                else:
                    full_path = os.path.normpath(os.path.join(base_dir, href))

                # Try to read the chapter
                try:
                    chapter_html = zip_file.read(full_path).decode('utf-8', errors='ignore')
                    chapter_md = html_to_markdown(chapter_html)
                    markdown_content += f"\n{chapter_md}\n"
                    print(f"    + {filename}")
                except Exception as e:
                    print(f"    ! {filename}: {e}")

            # Save to markdown
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"  Saved: {output_path}")
            return True

    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Extract all EPUB books."""
    print("=" * 70)
    print("EPUB to Markdown Extractor")
    print("=" * 70)

    success_count = 0
    for book in BOOKS:
        if extract_epub(book['epub'], book['output'], book['title']):
            success_count += 1

    print("\n" + "=" * 70)
    print(f"Complete: {success_count}/{len(BOOKS)} books extracted")
    print("=" * 70)
    return success_count == len(BOOKS)


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
