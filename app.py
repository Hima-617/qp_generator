import streamlit as st

from ui import render_header, render_sidebar
from generator import generate_question_paper
from utils import text_to_pdf_bytes


def main():
    st.set_page_config(
        page_title="Question Paper Generator",
        layout="wide",
    )

    render_header()

    grade, subject, num_mcq, num_short, num_long = render_sidebar()

    # Initialize session state
    if "qp_text" not in st.session_state:
        st.session_state["qp_text"] = ""
    if "answer_key_text" not in st.session_state:
        st.session_state["answer_key_text"] = ""

    st.markdown("### 🟦  Generate Question Paper")

    generate_clicked = st.button(
        "Generate Question Paper",
        use_container_width=True,
        type="primary",
    )

    if generate_clicked:
        qp_text, answer_key_text = generate_question_paper(
            grade=grade,
            subject=subject,
            num_mcq=num_mcq,
            num_short=num_short,
            num_long=num_long,
        )
        st.session_state["qp_text"] = qp_text
        st.session_state["answer_key_text"] = answer_key_text

    qp_text = st.session_state["qp_text"]
    answer_key_text = st.session_state["answer_key_text"]

    # (B) Question Paper Preview
    st.markdown("### 🟩  Question Paper Preview")
    if qp_text:
        st.text_area(
            "Question Paper",
            value=qp_text,
            height=400,
        )
    else:
        st.info("Generate a question paper to preview it here.")

    # (C) Answer Key Preview
    st.markdown("### 🟨  Answer Key Preview")
    if answer_key_text:
        st.text_area(
            "Answer Key",
            value=answer_key_text,
            height=300,
        )
    else:
        st.info("Generate a question paper to view the answer key here.")

    # (D) Download Section (4 buttons in a 2x2 grid)
    st.markdown("### 🟧  Download Section")

    if qp_text:
        qp_txt_bytes = qp_text.encode("utf-8")
        answer_txt_bytes = answer_key_text.encode("utf-8") if answer_key_text else b""

        qp_pdf_bytes = text_to_pdf_bytes(qp_text, title="Question Paper")
        answer_pdf_bytes = text_to_pdf_bytes(answer_key_text, title="Answer Key") if answer_key_text else b""
    else:
        qp_txt_bytes = b""
        answer_txt_bytes = b""
        qp_pdf_bytes = b""
        answer_pdf_bytes = b""

    # Row 1
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="Download QP (TXT)",
            data=qp_txt_bytes,
            file_name="question_paper.txt",
            mime="text/plain",
            disabled=not bool(qp_txt_bytes),
            use_container_width=True,
        )
    with col2:
        st.download_button(
            label="Download QP (PDF)",
            data=qp_pdf_bytes,
            file_name="question_paper.pdf",
            mime="application/pdf",
            disabled=not bool(qp_pdf_bytes),
            use_container_width=True,
        )

    # Row 2
    col3, col4 = st.columns(2)
    with col3:
        st.download_button(
            label="Download Answer Key (TXT)",
            data=answer_txt_bytes,
            file_name="answer_key.txt",
            mime="text/plain",
            disabled=not bool(answer_txt_bytes),
            use_container_width=True,
        )
    with col4:
        st.download_button(
            label="Download Answer Key (PDF)",
            data=answer_pdf_bytes,
            file_name="answer_key.pdf",
            mime="application/pdf",
            disabled=not bool(answer_pdf_bytes),
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
