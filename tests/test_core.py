"""Automated tests for TrigLab."""

import math

import pytest

from src.calculator import (
    calculate_trig,
    degrees_to_radians,
    radians_to_degrees,
    inverse_trig,
)
from src.triangle import (
    solve_from_angle_hypotenuse,
    solve_from_legs,
)
from src.quiz import check_answer

# --------------------------------------------------
# ANGLE CONVERSIONS
# --------------------------------------------------

def test_degrees_to_radians():
    assert math.isclose(
        degrees_to_radians(180),
        math.pi,
    )

def test_radians_to_degrees():
    assert math.isclose(
        radians_to_degrees(math.pi),
        180,
    )

def test_conversion_rejects_infinity():
    with pytest.raises(ValueError):
        degrees_to_radians(math.inf)

# --------------------------------------------------
# TRIGONOMETRIC CALCULATOR
# --------------------------------------------------

def test_sine_30_degrees():
    result = calculate_trig(30)
    assert math.isclose(result["sin"], 0.5)

def test_cosine_60_degrees():
    result = calculate_trig(60)
    assert math.isclose(result["cos"], 0.5)

def test_tangent_45_degrees():
    result = calculate_trig(45)
    assert math.isclose(result["tan"], 1.0)

def test_tangent_90_degrees_is_undefined():
    result = calculate_trig(90)
    assert result["tan"] is None

def test_radian_mode():
    result = calculate_trig(math.pi / 2, "radians")
    assert math.isclose(result["sin"], 1.0)

def test_invalid_angle_unit():
    with pytest.raises(ValueError):
        calculate_trig(30, "gradians")

def test_inverse_sine():
    result = inverse_trig(0.5, "asin")
    assert math.isclose(result, 30.0)

def test_inverse_sine_rejects_invalid_value():
    with pytest.raises(ValueError):
        inverse_trig(2.0, "asin")

# --------------------------------------------------
# TRIANGLE SOLVER
# --------------------------------------------------

def test_triangle_from_angle_and_hypotenuse():
    result = solve_from_angle_hypotenuse(30, 10)

    assert math.isclose(result["opposite"], 5.0)
    assert math.isclose(
        result["adjacent"],
        5 * math.sqrt(3),
    )

def test_triangle_from_two_legs():
    result = solve_from_legs(3, 4)

    assert math.isclose(result["hypotenuse"], 5.0)
    assert math.isclose(result["angle_degrees"], math.degrees(math.atan(3 / 4)))

def test_triangle_rejects_zero_length():
    with pytest.raises(ValueError):
        solve_from_legs(0, 4)

def test_triangle_rejects_invalid_angle():
    with pytest.raises(ValueError):
        solve_from_angle_hypotenuse(90, 10)

# --------------------------------------------------
# QUIZ
# --------------------------------------------------

def test_quiz_accepts_correct_answer():
    assert check_answer(0.5, 0.5)

def test_quiz_accepts_answer_within_tolerance():
    assert check_answer(0.51, 0.5)

def test_quiz_rejects_wrong_answer():
    assert not check_answer(0.8, 0.5)

def test_quiz_rejects_undefined_answer():
    assert not check_answer(1.0, None)

def test_quiz_rejects_nan():
    assert not check_answer(math.nan, 0.5)

def test_quiz_rejects_negative_tolerance():
    with pytest.raises(ValueError):
        check_answer(0.5, 0.5, tolerance=-0.1)