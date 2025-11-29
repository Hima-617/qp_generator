import random
from typing import List, Dict, Tuple

from question_bank import QUESTION_BANK
from utils import format_question_paper_text, format_answer_key_text


def _select_questions(
    pool: List[Dict],
    requested: int,
) -> List[Dict]:
    """
    Select exactly 'requested' questions (or as many as available if fewer),
    using a fresh local copy and shuffling it each time.
    """
    if requested <= 0 or not pool:
        return []

    local_copy = pool[:]  # IMPORTANT: do not mutate global pool
    random.shuffle(local_copy)
    requested = min(requested, len(local_copy))
    return local_copy[:requested]


def generate_question_paper(
    grade: str,
    subject: str,
    num_mcq: int,
    num_short: int,
    num_long: int,
) -> Tuple[str, str]:
    """
    Generate question paper and answer key text for the given configuration.
    """

    subject_data = QUESTION_BANK.get(grade, {}).get(subject)
    if not subject_data:
        raise ValueError(f"No questions configured for {grade} - {subject}")

    mcqs_pool = subject_data.get("mcq", [])
    short_pool = subject_data.get("short", [])
    long_pool = subject_data.get("long", [])

    selected_mcqs = _select_questions(mcqs_pool, num_mcq)
    selected_shorts = _select_questions(short_pool, num_short)
    selected_longs = _select_questions(long_pool, num_long)

    qp_text = format_question_paper_text(
        grade=grade,
        subject=subject,
        mcqs=selected_mcqs,
        shorts=selected_shorts,
        longs=selected_longs,
    )
    answer_key_text = format_answer_key_text(
        grade=grade,
        subject=subject,
        mcqs=selected_mcqs,
        shorts=selected_shorts,
        longs=selected_longs,
    )

    return qp_text, answer_key_text
