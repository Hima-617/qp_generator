from typing import List, Dict, Optional
import textwrap


# ---------- TEXT FORMATTING FOR QP & ANSWER KEY ----------

def format_question_paper_text(
    grade: str,
    subject: str,
    mcqs: List[Dict],
    shorts: List[Dict],
    longs: List[Dict],
) -> str:
    lines = []
    lines.append(f"{grade} - {subject}")
    lines.append("Question Paper")
    lines.append("-" * 60)
    lines.append("")

    q_num = 1

    if mcqs:
        lines.append("Section A: Multiple Choice Questions")
        lines.append("")
        for q in mcqs:
            lines.append(f"{q_num}. {q['question']}")
            for opt in q.get("options", []):
                lines.append(f"   {opt}")
            lines.append("")
            q_num += 1

    if shorts:
        lines.append("")
        lines.append("Section B: Short Answer Questions")
        lines.append("")
        for q in shorts:
            lines.append(f"{q_num}. {q['question']}")
            lines.append("")
            q_num += 1

    if longs:
        lines.append("")
        lines.append("Section C: Long Answer Questions")
        lines.append("")
        for q in longs:
            lines.append(f"{q_num}. {q['question']}")
            lines.append("")
            q_num += 1

    return "\n".join(lines).strip() + "\n"


def format_answer_key_text(
    grade: str,
    subject: str,
    mcqs: List[Dict],
    shorts: List[Dict],
    longs: List[Dict],
) -> str:
    lines = []
    lines.append(f"{grade} - {subject}")
    lines.append("Answer Key")
    lines.append("-" * 60)
    lines.append("")

    q_num = 1

    if mcqs:
        lines.append("Section A: Multiple Choice Questions")
        lines.append("")
        for q in mcqs:
            ans = q.get("answer", "")
            lines.append(f"{q_num}. {ans}")
            q_num += 1
        lines.append("")

    if shorts:
        lines.append("Section B: Short Answer Questions")
        lines.append("")
        for q in shorts:
            ans = q.get("answer", "")
            lines.append(f"{q_num}. {ans}")
            lines.append("")
            q_num += 1

    if longs:
        lines.append("Section C: Long Answer Questions")
        lines.append("")
        for q in longs:
            ans = q.get("answer", "")
            lines.append(f"{q_num}. {ans}")
            lines.append("")
            q_num += 1

    return "\n".join(lines).strip() + "\n"


# ---------- MINIMAL PDF GENERATOR (NO REPORTLAB) ----------

def _wrap_text_to_lines(text: str, max_chars_per_line: int = 90) -> List[str]:
    """
    Wrap text into lines by character count. This is a simple approximation
    for PDF text layout without dealing with font metrics.
    """
    all_lines: List[str] = []
    for line in text.splitlines():
        if not line:
            all_lines.append("")
            continue
        wrapped = textwrap.wrap(line, width=max_chars_per_line) or [""]
        all_lines.extend(wrapped)
    return all_lines


def text_to_pdf_bytes(text: str, title: Optional[str] = None) -> bytes:
    """
    Create a simple, valid PDF from plain text.

    Requirements:
    - No external libraries like reportlab.
    - Uses Helvetica font.
    - Wraps long lines.
    - Supports multiple pages.
    - Produces valid xref offsets.
    """

    if not text:
        text = ""

    # Prepare text lines
    lines = _wrap_text_to_lines(text, max_chars_per_line=90)

    # Basic A4 dimensions (points)
    page_width = 595
    page_height = 842
    margin_left = 50
    margin_top = 50
    line_height = 14

    usable_height = page_height - 2 * margin_top
    max_lines_per_page = max(int(usable_height // line_height), 1)

    # Split lines into pages
    pages_lines: List[List[str]] = []
    current_page: List[str] = []
    for line in lines:
        if len(current_page) >= max_lines_per_page:
            pages_lines.append(current_page)
            current_page = []
        current_page.append(line)
    if current_page:
        pages_lines.append(current_page)

    num_pages = max(len(pages_lines), 1)

    # Object numbering:
    # 1: Catalog
    # 2: Pages
    # 3: Font
    # Then for each page:
    #   page_obj_id, contents_obj_id
    total_objects = 3 + 2 * num_pages

    page_obj_ids = []
    contents_obj_ids = []

    next_id = 4
    for _ in range(num_pages):
        page_obj_ids.append(next_id)
        contents_obj_ids.append(next_id + 1)
        next_id += 2

    # Helper to track offsets and build PDF
    pdf_bytes = bytearray()
    offsets = [0] * (total_objects + 1)  # index 0 unused but needed for xref

    def _write_line(s: str):
        pdf_bytes.extend(s.encode("latin-1"))

    def _write_obj(obj_id: int, body: str):
        offsets[obj_id] = len(pdf_bytes)
        _write_line(f"{obj_id} 0 obj\n")
        _write_line(body)
        _write_line("\nendobj\n")

    # PDF Header
    _write_line("%PDF-1.4\n")

    # 1: Catalog
    catalog_body = f"<< /Type /Catalog /Pages 2 0 R >>"
    _write_obj(1, catalog_body)

    # 2: Pages (will reference page objects)
    kids_str = " ".join(f"{pid} 0 R" for pid in page_obj_ids)
    pages_body = f"<< /Type /Pages /Kids [ {kids_str} ] /Count {num_pages} >>"
    _write_obj(2, pages_body)

    # 3: Font (Helvetica)
    font_body = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"
    _write_obj(3, font_body)

    # Page & content objects
    for idx, page_lines in enumerate(pages_lines):
        page_id = page_obj_ids[idx]
        content_id = contents_obj_ids[idx]

        # Build content stream for this page
        content_text_lines = []
        content_text_lines.append("BT")
        content_text_lines.append("/F1 12 Tf")
        # Start position: (margin_left, top from bottom)
        # PDF origin is bottom-left, so y coordinate downwards:
        start_y = page_height - margin_top
        content_text_lines.append(f"{margin_left} {start_y} Td")

        first_line = True
        for line in page_lines:
            # Escape special characters
            escaped = (
                line.replace("\\", "\\\\")
                    .replace("(", "\\(")
                    .replace(")", "\\)")
            )
            if first_line:
                content_text_lines.append(f"({escaped}) Tj")
                first_line = False
            else:
                content_text_lines.append(f"0 -{line_height} Td")
                content_text_lines.append(f"({escaped}) Tj")

        content_text_lines.append("ET")
        content_stream_text = "\n".join(content_text_lines) + "\n"
        content_stream_bytes = content_stream_text.encode("latin-1")
        length = len(content_stream_bytes)

        # Content object
        content_body = (
            f"<< /Length {length} >>\n"
            f"stream\n"
            f"{content_stream_text}"
            f"endstream"
        )
        _write_obj(content_id, content_body)

        # Page object
        page_body = (
            "<< /Type /Page /Parent 2 0 R "
            f"/MediaBox [0 0 {page_width} {page_height}] "
            "/Resources << /Font << /F1 3 0 R >> >> "
            f"/Contents {content_id} 0 R >>"
        )
        _write_obj(page_id, page_body)

    # XRef table
    xref_start = len(pdf_bytes)
    _write_line(f"xref\n")
    _write_line(f"0 {total_objects + 1}\n")
    _write_line("0000000000 65535 f \n")  # object 0

    for obj_id in range(1, total_objects + 1):
        offset = offsets[obj_id]
        _write_line(f"{offset:010d} 00000 n \n")

    # Trailer
    if title:
        trailer = (
            "trailer\n"
            f"<< /Size {total_objects + 1} /Root 1 0 R "
            f"/Info << /Title ({title}) >> >>\n"
        )
    else:
        trailer = (
            "trailer\n"
            f"<< /Size {total_objects + 1} /Root 1 0 R >>\n"
        )

    _write_line(trailer)
    _write_line(f"startxref\n{xref_start}\n%%EOF\n")

    return bytes(pdf_bytes)
