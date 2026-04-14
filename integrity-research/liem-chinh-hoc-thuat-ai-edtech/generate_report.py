#!/usr/bin/env python3
"""Generate research report from JSON results."""
import json
import os
import re
import yaml

TOPIC_DIR = "/home/ubuntu/nhannht-projects/hcmus/semester2/intro-edu-science/liem-chinh-hoc-thuat-ai-edtech"
RESULTS_DIR = os.path.join(TOPIC_DIR, "results")
FIELDS_YAML = os.path.join(TOPIC_DIR, "fields.yaml")
OUTPUT_MD = os.path.join(TOPIC_DIR, "report.md")

CATEGORY_MAPPING = {
    "Định nghĩa & Khái niệm": ["dinh_nghia_khai_niem", "dinh_nghia", "phan_loai", "lich_su_khai_niem"],
    "Bằng chứng thực tế": ["bang_chung_thuc_te", "ten_truong_hop", "dien_bien", "ket_qua_xu_ly", "con_so_thong_ke"],
    "Tác hại & Hậu quả": ["tac_hai_hau_qua", "hai_cho_nguoi_hoc", "hai_cho_nghien_cuu", "hai_cho_xa_hoi"],
    "Phát hiện & Công cụ": ["phat_hien_cong_cu", "cong_cu_phat_hien", "han_che_cong_cu", "watermarking"],
    "Phòng ngừa & Giải pháp": ["phong_ngua_giai_phap", "thiet_ke_bai_tap", "chinh_sach_truong_hoc", "van_hoa_to_chuc", "ai_literacy"],
    "Khung pháp lý & Đạo đức": ["khung_phap_ly_dao_duc", "khung_quoc_te", "phap_luat_viet_nam", "chinh_sach_chau_a"],
    "Góc nhìn EdTech": ["goc_nhin_edtech", "ai_tutor_vs_ai_cheater", "edtech_company_policies", "de_xuat_nha_nghien_cuu"],
    "Nguồn tài liệu": ["nguon_tai_lieu", "bai_bao_khoa_hoc", "sach_tham_khao", "nguon_viet_nam"],
}

FIELD_LABELS = {
    "dinh_nghia": "Định nghĩa",
    "phan_loai": "Phân loại vi phạm",
    "lich_su_khai_niem": "Lịch sử khái niệm",
    "ten_truong_hop": "Tên trường hợp",
    "dien_bien": "Diễn biến",
    "ket_qua_xu_ly": "Kết quả xử lý",
    "con_so_thong_ke": "Con số thống kê",
    "hai_cho_nguoi_hoc": "Hại cho người học",
    "hai_cho_nghien_cuu": "Hại cho nghiên cứu",
    "hai_cho_xa_hoi": "Hại cho xã hội",
    "cong_cu_phat_hien": "Công cụ phát hiện",
    "han_che_cong_cu": "Hạn chế công cụ",
    "watermarking": "LLM Watermarking",
    "thiet_ke_bai_tap": "Thiết kế bài tập",
    "chinh_sach_truong_hoc": "Chính sách trường học",
    "van_hoa_to_chuc": "Văn hóa tổ chức",
    "ai_literacy": "AI Literacy",
    "khung_quoc_te": "Khung quốc tế",
    "phap_luat_viet_nam": "Pháp luật Việt Nam",
    "chinh_sach_chau_a": "Chính sách châu Á",
    "ai_tutor_vs_ai_cheater": "AI tutor vs AI cheater",
    "edtech_company_policies": "Chính sách EdTech companies",
    "de_xuat_nha_nghien_cuu": "Đề xuất nhà nghiên cứu EdTech",
    "bai_bao_khoa_hoc": "Bài báo khoa học",
    "sach_tham_khao": "Sách tham khảo",
    "nguon_viet_nam": "Nguồn Việt Nam",
}

INTERNAL_KEYS = {"uncertain", "_source_file", "id", "name", "type", "category",
                 "institution", "year", "author", "organization", "url", "doi",
                 "specialty", "key_work", "note", "summary", "outcome", "gap",
                 "effective", "launched", "creator", "method", "claimed_fp",
                 "actual_fp", "users", "status", "mechanisms", "adopters",
                 "limitation", "model", "approach", "standards", "vietnam_connection",
                 "tenets", "elements", "values", "tiers", "principles",
                 "article_20", "key_argument", "key_finding", "key_recommendation",
                 "education_provisions", "relevant_sections", "key_provisions",
                 "official_accuracy", "false_positive", "controversy", "isbn",
                 "pages", "adopted_by", "issuer", "year_founded"}

TOC_FIELDS = ["type", "institution", "year", "category"]


def slugify(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')


def is_uncertain(value, uncertain_list):
    if value is None or value == "":
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    return False


def format_value(value):
    if isinstance(value, list):
        if not value:
            return ""
        if all(isinstance(i, dict) for i in value):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items()]
                lines.append(" | ".join(parts))
            return "\n".join(f"- {l}" for l in lines)
        if len(value) <= 5:
            return ", ".join(str(i) for i in value)
        return "\n".join(f"- {i}" for i in value)
    if isinstance(value, dict):
        parts = []
        for k, v in value.items():
            parts.append(f"**{k}**: {v}")
        return "; ".join(parts)
    text = str(value)
    if len(text) > 150:
        return f"> {text}"
    return text


def get_field(data, field_name, uncertain_list):
    val = data.get(field_name)
    if val is not None and not is_uncertain(val, uncertain_list):
        return val
    # search nested
    for v in data.values():
        if isinstance(v, dict):
            inner = v.get(field_name)
            if inner is not None and not is_uncertain(inner, uncertain_list):
                return inner
    return None


def load_all_items():
    items = []
    for fname in sorted(os.listdir(RESULTS_DIR)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(RESULTS_DIR, fname)) as f:
            try:
                data = json.load(f)
                data["_source_file"] = fname
                items.append(data)
            except json.JSONDecodeError as e:
                print(f"  WARN: Could not parse {fname}: {e}")
    return items


def build_toc(items):
    lines = ["## Table of Contents\n"]
    for i, item in enumerate(items, 1):
        name = item.get("name", item.get("_source_file", f"Item {i}"))
        anchor = slugify(name)
        meta_parts = []
        for field in TOC_FIELDS:
            val = item.get(field)
            if val and not is_uncertain(val, item.get("uncertain", [])):
                meta_parts.append(f"**{field}**: {val}")
        meta = " | ".join(meta_parts) if meta_parts else ""
        if meta:
            lines.append(f"{i}. [{name}](#{anchor}) — {meta}")
        else:
            lines.append(f"{i}. [{name}](#{anchor})")
    return "\n".join(lines)


def build_item_section(item):
    uncertain_list = item.get("uncertain", [])
    name = item.get("name", "Unknown")
    anchor = slugify(name)
    lines = [f"---\n", f"## {name} {{#{anchor}}}\n"]

    # Quick metadata table
    meta_rows = []
    for field in TOC_FIELDS + ["author", "organization", "institution", "specialty", "url", "doi"]:
        val = item.get(field)
        if val and not is_uncertain(val, uncertain_list) and field not in ["name"]:
            meta_rows.append((field.capitalize(), val))
    if meta_rows:
        lines.append("| Field | Value |")
        lines.append("|---|---|")
        for k, v in meta_rows:
            lines.append(f"| {k} | {v} |")
        lines.append("")

    # Summary/key info boxes
    for quick_key in ["summary", "key_argument", "key_finding", "key_recommendation", "key_work"]:
        val = item.get(quick_key)
        if val and not is_uncertain(val, uncertain_list):
            lines.append(f"> **{quick_key.replace('_', ' ').title()}:** {val}\n")

    # Defined fields by category
    all_defined_fields = set()
    for cat_name, field_keys in CATEGORY_MAPPING.items():
        cat_lines = []
        for fk in field_keys:
            if fk in uncertain_list:
                continue
            val = get_field(item, fk, uncertain_list)
            if val is None:
                continue
            all_defined_fields.add(fk)
            label = FIELD_LABELS.get(fk, fk.replace("_", " ").title())
            formatted = format_value(val)
            if "\n" in formatted or formatted.startswith(">"):
                cat_lines.append(f"**{label}:**\n\n{formatted}\n")
            else:
                cat_lines.append(f"**{label}:** {formatted}\n")
        if cat_lines:
            lines.append(f"### {cat_name}\n")
            lines.extend(cat_lines)

    # Extra fields not in defined categories
    extra = {}
    for k, v in item.items():
        if k in INTERNAL_KEYS or k in all_defined_fields:
            continue
        if k == "uncertain" or k.startswith("_"):
            continue
        if is_uncertain(v, uncertain_list) or k in uncertain_list:
            continue
        if isinstance(v, dict) and all(kk in CATEGORY_MAPPING or kk in FIELD_LABELS for kk in v):
            continue
        extra[k] = v

    if extra:
        lines.append("### Other Info\n")
        for k, v in extra.items():
            label = k.replace("_", " ").title()
            formatted = format_value(v)
            if "\n" in formatted or formatted.startswith(">"):
                lines.append(f"**{label}:**\n\n{formatted}\n")
            else:
                lines.append(f"**{label}:** {formatted}\n")

    # Uncertain fields list
    if uncertain_list:
        lines.append("### Uncertain Fields\n")
        for u in uncertain_list:
            lines.append(f"- {u}")
        lines.append("")

    return "\n".join(lines)


def main():
    print("Loading items...")
    items = load_all_items()
    print(f"  Found {len(items)} items")

    lines = [
        "# Research Report: Liêm chính học thuật và gian lận AI trong nghiên cứu EdTech\n",
        f"*Generated from {len(items)} research items*\n",
        build_toc(items),
        "\n---\n",
    ]

    for i, item in enumerate(items, 1):
        name = item.get("name", f"Item {i}")
        print(f"  [{i}/{len(items)}] {name[:60]}")
        lines.append(build_item_section(item))

    report = "\n".join(lines)
    with open(OUTPUT_MD, "w") as f:
        f.write(report)
    print(f"\nReport saved to: {OUTPUT_MD}")
    print(f"Size: {len(report):,} chars, ~{len(report.split())//130} pages (est.)")


if __name__ == "__main__":
    main()
