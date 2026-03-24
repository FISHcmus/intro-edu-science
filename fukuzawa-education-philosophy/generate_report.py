#!/usr/bin/env python3
"""Generate markdown report from Fukuzawa education philosophy research JSON files."""

import json
import glob
import os
import re
import yaml

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
FIELDS_PATH = os.path.join(os.path.dirname(__file__), "fields.yaml")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "report.md")

# Category mapping: fields.yaml key -> possible JSON keys
CATEGORY_MAPPING = {
    "concept_core": ["concept_core", "Concept Core"],
    "intellectual_origins": ["intellectual_origins", "Intellectual Origins"],
    "educational_implication": ["educational_implication", "Educational Implication"],
    "institutional_expression": ["institutional_expression", "Institutional Expression"],
    "historical_impact": ["historical_impact", "Historical Impact"],
    "relevance_to_vietnam": ["relevance_to_vietnam", "Relevance to Vietnam"],
    "contradictions_and_critiques": ["contradictions_and_critiques", "Contradictions and Critiques"],
    "empirical_methodology": ["empirical_methodology", "Empirical Methodology"],
    "transnational_influence": ["transnational_influence", "Transnational Influence"],
    "civic_discourse": ["civic_discourse", "Civic Discourse"],
}

# Internal/meta fields to skip
SKIP_KEYS = {"uncertain", "_source_file"} | set(CATEGORY_MAPPING.keys())

# Human-readable category titles
CATEGORY_TITLES = {
    "concept_core": "Core Concept",
    "intellectual_origins": "Intellectual Origins",
    "educational_implication": "Educational Implications",
    "institutional_expression": "Institutional Expression",
    "historical_impact": "Historical Impact",
    "relevance_to_vietnam": "Relevance to Vietnam",
    "contradictions_and_critiques": "Contradictions & Critiques",
    "empirical_methodology": "Empirical Methodology",
    "transnational_influence": "Transnational Influence",
    "civic_discourse": "Civic Discourse",
}

# Human-readable field titles
FIELD_TITLES = {
    "concept_name": "Concept Name",
    "original_japanese": "Original Japanese",
    "definition": "Definition",
    "key_quote": "Key Quote",
    "source_work": "Source Work",
    "western_influences": "Western Influences",
    "japanese_context": "Japanese Context",
    "what_it_reacted_against": "What It Reacted Against",
    "what_should_be_taught": "What Should Be Taught",
    "how_should_it_be_taught": "How Should It Be Taught",
    "role_of_teacher": "Role of Teacher",
    "role_of_student": "Role of Student",
    "how_keio_embodied_this": "How Keio Embodied This",
    "other_institutions": "Other Institutions",
    "concrete_actions": "Concrete Actions",
    "effect_on_meiji_japan": "Effect on Meiji Japan",
    "effect_on_modern_education": "Effect on Modern Education",
    "reception_and_criticism": "Reception & Criticism",
    "parallel_to_vietnamese_education": "Parallels to Vietnamese Education",
    "comparison_with_vn_education_law": "Comparison with VN Education Law",
    "applicability_today": "Applicability Today",
    "internal_tensions": "Internal Tensions",
    "scholarly_debates": "Scholarly Debates",
    "what_critics_say": "What Critics Say",
    "observation_method": "Observation Method",
    "relationship_to_scientific_method": "Relationship to Scientific Method",
    "vietnam_adoption": "Vietnam Adoption",
    "korea_adoption": "Korea Adoption",
    "china_comparison": "China Comparison",
    "speech_and_debate": "Speech & Debate",
    "democratic_citizenship": "Democratic Citizenship",
}


def slugify(text):
    """Convert text to anchor-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    return text


def is_uncertain(field_name, value, uncertain_list):
    """Check if a field should be skipped due to uncertainty."""
    if value is None or value == "":
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    if field_name in uncertain_list:
        return True
    return False


def format_value(value):
    """Format a field value for markdown display."""
    if isinstance(value, list):
        if len(value) == 0:
            return ""
        if isinstance(value[0], dict):
            lines = []
            for item in value:
                parts = [f"**{k}:** {v}" for k, v in item.items()]
                lines.append("- " + " | ".join(parts))
            return "\n".join(lines)
        if len(value) <= 3 and all(len(str(v)) < 50 for v in value):
            return ", ".join(str(v) for v in value)
        return "\n".join(f"- {v}" for v in value)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"- **{FIELD_TITLES.get(k, k)}:** {v}")
        return "\n".join(lines)
    value = str(value)
    if len(value) > 200:
        return f"\n> {value}\n"
    return value


def find_category_data(data, category_key):
    """Find category data in JSON, supporting flat and nested structures."""
    aliases = CATEGORY_MAPPING.get(category_key, [category_key])
    for alias in aliases:
        if alias in data:
            return data[alias]
    # Traverse all nested dicts
    for k, v in data.items():
        if isinstance(v, dict):
            for alias in aliases:
                if alias in v:
                    return v[alias]
    return {}


def load_fields():
    """Load field definitions from fields.yaml."""
    with open(FIELDS_PATH, 'r') as f:
        return yaml.safe_load(f)


def load_results():
    """Load all JSON result files, sorted by filename."""
    results = []
    for path in sorted(glob.glob(os.path.join(RESULTS_DIR, "*.json"))):
        with open(path, 'r') as f:
            data = json.load(f)
        data["_source_file"] = os.path.basename(path)
        results.append(data)
    return results


def get_item_name(data):
    """Extract item name from data."""
    cc = find_category_data(data, "concept_core")
    if isinstance(cc, dict):
        return cc.get("concept_name", data["_source_file"].replace(".json", "").replace("_", " "))
    return data["_source_file"].replace(".json", "").replace("_", " ")


def get_source_work(data):
    """Extract source work from data."""
    cc = find_category_data(data, "concept_core")
    if isinstance(cc, dict):
        val = cc.get("source_work", "")
        if isinstance(val, str) and "[uncertain]" not in val:
            return val
    return ""


def generate_report():
    fields_def = load_fields()
    results = load_results()

    lines = []
    lines.append("# The Philosophy of Fukuzawa Yukichi on Education")
    lines.append("")
    lines.append("*Research report generated from 18 structured research items.*")
    lines.append("")

    # TOC
    lines.append("## Table of Contents")
    lines.append("")
    for i, data in enumerate(results, 1):
        name = get_item_name(data)
        source = get_source_work(data)
        slug = slugify(name)
        source_str = f" — *{source}*" if source else ""
        lines.append(f"{i}. [{name}](#{slug}){source_str}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed content
    category_order = [
        "concept_core", "intellectual_origins", "educational_implication",
        "institutional_expression", "historical_impact", "relevance_to_vietnam",
        "contradictions_and_critiques", "empirical_methodology",
        "transnational_influence", "civic_discourse",
    ]

    for i, data in enumerate(results, 1):
        name = get_item_name(data)
        uncertain_list = data.get("uncertain", [])
        # Normalize uncertain list - could be list of strings or detailed descriptions
        uncertain_names = set()
        for u in uncertain_list:
            if isinstance(u, str):
                # Extract field name from descriptions like "korea_adoption (details...)"
                match = re.match(r'^(\w+)', u)
                if match:
                    uncertain_names.add(match.group(1))

        lines.append(f"## {i}. {name}")
        lines.append("")

        for cat_key in category_order:
            cat_data = find_category_data(data, cat_key)
            if not cat_data or not isinstance(cat_data, dict):
                continue

            cat_title = CATEGORY_TITLES.get(cat_key, cat_key)
            has_content = False
            cat_lines = []

            for field_name, field_value in cat_data.items():
                if is_uncertain(field_name, field_value, uncertain_names):
                    continue
                formatted = format_value(field_value)
                if not formatted:
                    continue
                has_content = True
                field_title = FIELD_TITLES.get(field_name, field_name.replace("_", " ").title())
                cat_lines.append(f"**{field_title}:**")
                cat_lines.append(formatted)
                cat_lines.append("")

            if has_content:
                lines.append(f"### {cat_title}")
                lines.append("")
                lines.extend(cat_lines)

        # Collect extra fields not in category mapping
        extra_lines = []
        for k, v in data.items():
            if k in SKIP_KEYS:
                continue
            if k not in CATEGORY_MAPPING and not isinstance(v, dict):
                if not is_uncertain(k, v, uncertain_names):
                    formatted = format_value(v)
                    if formatted:
                        field_title = FIELD_TITLES.get(k, k.replace("_", " ").title())
                        extra_lines.append(f"**{field_title}:** {formatted}")
                        extra_lines.append("")

        if extra_lines:
            lines.append("### Other Info")
            lines.append("")
            lines.extend(extra_lines)

        lines.append("---")
        lines.append("")

    # Write report
    with open(OUTPUT_PATH, 'w') as f:
        f.write("\n".join(lines))

    print(f"Report generated: {OUTPUT_PATH}")
    print(f"Items: {len(results)}")
    print(f"Total lines: {len(lines)}")


if __name__ == "__main__":
    generate_report()
