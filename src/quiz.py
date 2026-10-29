"""Randomized trigonometry quiz."""

import math
import random

SPECIAL_ANGLES = [0, 30, 45, 60, 90, 120, 135, 150, 180]

def generate_question() -> dict[str, float | str]:
    """Generate a question about a special angle."""
    angle = random.choice(SPECIAL_ANGLES)
    function = random.choice(["sin", "cos", "tan"])

    radians = math.radians(angle)

    if function == "sin":
        answer = math.sin(radians)
    elif function == "cos":
        answer = math.cos(radians)
    else:
        answer = (
            None
            if math.isclose(math.cos(radians), 0.0, abs_tol=1e-12)
            else math.tan(radians)
        )

    return {
        "angle": angle,
        "function": function,
        "answer": answer,
    }

def check_answer(
    user_answer: float,
    correct_answer: float | None,
    tolerance: float = 0.02,
) -> bool:
    """Check a numerical answer within a defined tolerance."""
    if not math.isfinite(user_answer):
        return False

    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("Tolerance must be finite and non-negative.")

    if correct_answer is None:
        return False

    if not math.isfinite(correct_answer):
        raise ValueError("Correct answer must be finite.")

    return math.isclose(
        user_answer,
        correct_answer,
        rel_tol=0.0,
        abs_tol=tolerance,
    )