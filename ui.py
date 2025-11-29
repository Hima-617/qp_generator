import streamlit as st
from question_bank import QUESTION_BANK, get_subjects_for_grade, get_question_type_counts


def render_header():
    st.title("📝 Question Paper Generator")
    st.write(
        "Generate customized question papers and answer keys "
        "for Grades 1–12 and B.Tech subjects."
    )


def render_sidebar():
    st.sidebar.header("⚙️ Configuration")

    # Grades: ensure sorted order Grade 1..Grade 12, then B.Tech
    grade_keys = sorted(
        [g for g in QUESTION_BANK.keys() if g.startswith("Grade")],
        key=lambda x: int(x.split()[1]),
    )
    if "B.Tech" in QUESTION_BANK:
        grade_keys.append("B.Tech")

    grade = st.sidebar.selectbox("Select Grade / Level", grade_keys, index=0)

    subjects = get_subjects_for_grade(grade)
    subject = st.sidebar.selectbox("Select Subject", subjects, index=0)

    counts = get_question_type_counts(grade, subject)
    max_mcq = counts.get("mcq", 0)
    max_short = counts.get("short", 0)
    max_long = counts.get("long", 0)

    if max_mcq == 0 or max_short == 0 or max_long == 0:
        st.sidebar.error(
            "Selected grade/subject does not have enough questions configured."
        )

    st.sidebar.markdown("---")

    num_mcq = st.sidebar.slider(
        "Number of MCQs",
        min_value=0,
        max_value=max_mcq,
        value=min(5, max_mcq),
        step=1,
    )

    num_short = st.sidebar.slider(
        "Number of Short Answer Questions",
        min_value=0,
        max_value=max_short,
        value=min(3, max_short),
        step=1,
    )

    num_long = st.sidebar.slider(
        "Number of Long Answer Questions",
        min_value=0,
        max_value=max_long,
        value=min(2, max_long),
        step=1,
    )

    return grade, subject, num_mcq, num_short, num_long
