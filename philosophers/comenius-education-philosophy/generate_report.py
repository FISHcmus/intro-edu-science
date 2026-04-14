#!/usr/bin/env python3
"""Generate markdown report from Comenius education philosophy research JSON results."""

import json
import os
import re
import glob
import yaml

TOPIC_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(TOPIC_DIR, "results")
FIELDS_PATH = os.path.join(TOPIC_DIR, "fields.yaml")
OUTLINE_PATH = os.path.join(TOPIC_DIR, "outline.yaml")
OUTPUT_PATH = os.path.join(TOPIC_DIR, "report.md")

# Category mapping: display_name -> possible JSON keys
CATEGORY_MAPPING = {
    "Basic Info": ["basic_info", "Basic Info", "basicInfo"],
    "Philosophical Foundation": ["philosophical_foundation", "Philosophical Foundation", "philosophicalFoundation"],
    "Educational Principles": ["educational_principles", "Educational Principles", "educationalPrinciples"],
    "Developmental Theory": ["developmental_theory", "Developmental Theory", "developmentalTheory"],
    "Historical Context": ["historical_context", "Historical Context", "historicalContext"],
    "Influence & Legacy": ["influence_and_legacy", "Influence & Legacy", "influenceAndLegacy", "influence_legacy"],
    "Critiques & Controversies": ["critiques_and_controversies", "Critiques & Controversies", "critiquesAndControversies", "critiques_controversies"],
    "Comparative Analysis": ["comparative_analysis", "Comparative Analysis", "comparativeAnalysis"],
    "Key Quotes": ["key_quotes", "Key Quotes", "keyQuotes"],
    "Vietnamese Relevance": ["vietnamese_relevance", "Vietnamese Relevance", "vietnameseRelevance"],
}

INTERNAL_FIELDS = {"_source_file", "uncertain"}
NESTED_TOP_KEYS = set()
for keys in CATEGORY_MAPPING.values():
    NESTED_TOP_KEYS.update(keys)


def load_fields_yaml():
    with open(FIELDS_PATH, "r") as f:
        data = yaml.safe_load(f)
    categories = {}
    all_field_names = set()
    for cat_key, cat_data in data.get("categories", {}).items():
        display_name = cat_data.get("display_name", cat_key)
        fields = []
        for field in cat_data.get("fields", []):
            fields.append(field)
            all_field_names.add(field["name"])
        categories[display_name] = {"key": cat_key, "fields": fields}
    return categories, all_field_names


def load_outline():
    with open(OUTLINE_PATH, "r") as f:
        data = yaml.safe_load(f)
    items_info = {}
    for item in data.get("items", []):
        items_info[item["name"]] = item.get("category", "")
    return data.get("topic", "Research Report"), items_info


def find_field_value(data, field_name, category_keys=None):
    """Look up field value: top-level -> category dict -> traverse all nested dicts."""
    if field_name in data and not isinstance(data[field_name], dict):
        return data[field_name]
    if category_keys:
        for ck in category_keys:
            if ck in data and isinstance(data[ck], dict):
                if field_name in data[ck]:
                    return data[ck][field_name]
    for k, v in data.items():
        if isinstance(v, dict) and field_name in v:
            return v[field_name]
    return None


def is_uncertain(value, field_name, uncertain_list):
    if value is None or value == "":
        return True
    if field_name in uncertain_list:
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    return False


def format_value(value, indent=0):
    """Format complex values for markdown display."""
    if value is None or value == "":
        return ""
    if isinstance(value, list):
        if len(value) == 0:
            return ""
        if all(isinstance(item, dict) for item in value):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items() if v]
                lines.append("  - " + " | ".join(parts))
            return "\n" + "\n".join(lines)
        if all(isinstance(item, str) for item in value):
            if sum(len(s) for s in value) < 120 and len(value) <= 5:
                return ", ".join(value)
            else:
                return "\n" + "\n".join(f"  - {item}" for item in value)
        return "\n" + "\n".join(f"  - {str(item)}" for item in value)
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if isinstance(v, (dict, list)):
                formatted = format_value(v, indent + 1)
                lines.append(f"  - **{k}**: {formatted}")
            else:
                lines.append(f"  - **{k}**: {v}")
        return "\n" + "\n".join(lines)
    value_str = str(value)
    if len(value_str) > 200:
        return "\n\n> " + value_str.replace("\n", "\n> ")
    return value_str


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def generate_report():
    topic, items_info = load_outline()
    categories, all_field_names = load_fields_yaml()

    json_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "*.json")))
    if not json_files:
        print("No JSON files found in results/")
        return

    all_data = []
    for jf in json_files:
        with open(jf, "r") as f:
            data = json.load(f)
        data["_source_file"] = os.path.basename(jf)
        all_data.append(data)

    lines = []
    lines.append(f"# {topic}\n")
    lines.append(f"*Research report generated from {len(all_data)} items*\n")
    lines.append("---\n")

    # Table of Contents
    lines.append("## Table of Contents\n")
    for i, data in enumerate(all_data, 1):
        name = find_field_value(data, "name") or data["_source_file"].replace(".json", "").replace("_", " ")
        year = find_field_value(data, "year") or ""
        item_type = find_field_value(data, "type") or ""
        # Find category from outline
        category = ""
        for outline_name, cat in items_info.items():
            if name and (outline_name.lower() in name.lower() or name.lower() in outline_name.lower()):
                category = cat
                break
        slug = slugify(name)
        parts = [f"[{name}](#{slug})"]
        if year:
            parts.append(f"Year: {year}")
        if item_type:
            parts.append(f"Type: {item_type}")
        if category:
            parts.append(f"Category: {category}")
        lines.append(f"{i}. {' | '.join(parts)}")
    lines.append("")

    # Detailed content
    lines.append("---\n")
    lines.append("## Detailed Content\n")

    for i, data in enumerate(all_data, 1):
        name = find_field_value(data, "name") or data["_source_file"].replace(".json", "").replace("_", " ")
        uncertain_list = data.get("uncertain", [])
        if isinstance(uncertain_list, dict):
            uncertain_list = list(uncertain_list.keys())
        elif not isinstance(uncertain_list, list):
            uncertain_list = []

        lines.append(f"### {i}. {name}\n")

        # Process each category from fields.yaml
        for display_name, cat_info in categories.items():
            cat_key = cat_info["key"]
            fields = cat_info["fields"]
            possible_keys = CATEGORY_MAPPING.get(display_name, [cat_key])

            section_lines = []
            for field in fields:
                fname = field["name"]
                value = find_field_value(data, fname, possible_keys)
                if is_uncertain(value, fname, uncertain_list):
                    continue
                formatted = format_value(value)
                if formatted:
                    section_lines.append(f"- **{fname}**: {formatted}")

            if section_lines:
                lines.append(f"#### {display_name}\n")
                lines.extend(section_lines)
                lines.append("")

        # Extra fields not in fields.yaml
        extra_lines = []
        all_keys_in_json = set()

        def collect_keys(d, prefix=""):
            for k, v in d.items():
                if k in INTERNAL_FIELDS or k in NESTED_TOP_KEYS:
                    continue
                if isinstance(v, dict) and k not in all_field_names:
                    collect_keys(v, prefix + k + ".")
                else:
                    all_keys_in_json.add(k)

        collect_keys(data)
        extra_fields = all_keys_in_json - all_field_names
        for ef in sorted(extra_fields):
            value = find_field_value(data, ef)
            if is_uncertain(value, ef, uncertain_list):
                continue
            if value is not None and value != "":
                formatted = format_value(value)
                if formatted:
                    extra_lines.append(f"- **{ef}**: {formatted}")

        if extra_lines:
            lines.append(f"#### Other Info\n")
            lines.extend(extra_lines)
            lines.append("")

        # Uncertain fields
        if uncertain_list:
            lines.append(f"#### Uncertain Fields\n")
            for uf in uncertain_list:
                lines.append(f"- {uf}")
            lines.append("")

        lines.append("---\n")

    report = "\n".join(lines)
    with open(OUTPUT_PATH, "w") as f:
        f.write(report)

    word_count = len(report.split())
    line_count = len(lines)
    print(f"Report generated: {OUTPUT_PATH}")
    print(f"Words: {word_count:,}, Lines: {line_count:,}, Items: {len(all_data)}")


if __name__ == "__main__":
    generate_report()
