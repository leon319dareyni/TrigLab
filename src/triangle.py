"""Right-triangle calculations."""

import math

def _validate_positive(value: float, name: str) -> None:
    """Validate a positive, finite measurement."""
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite.")

def solve_from_angle_hypotenuse(
    angle_degrees: float,
    hypotenuse: float,
) -> dict[str, float]:
    """
    Find the opposite and adjacent sides from an acute angle
    and the hypotenuse.
    """
    _validate_positive(hypotenuse, "Hypotenuse")

    if (
        not math.isfinite(angle_degrees)
        or not 0 < angle_degrees < 90
    ):
        raise ValueError("Angle must be between 0 and 90 degrees.")

    angle = math.radians(angle_degrees)

    opposite = hypotenuse * math.sin(angle)
    adjacent = hypotenuse * math.cos(angle)

    return {
        "opposite": opposite,
        "adjacent": adjacent,
        "hypotenuse": hypotenuse,
        "angle_degrees": angle_degrees,
    }

def solve_from_legs(
    opposite: float,
    adjacent: float,
) -> dict[str, float]:
    """Find the hypotenuse and acute angles from two legs."""
    _validate_positive(opposite, "Opposite side")
    _validate_positive(adjacent, "Adjacent side")

    hypotenuse = math.hypot(opposite, adjacent)

    angle_degrees = math.degrees(
        math.atan2(opposite, adjacent)
    )

    other_angle_degrees = 90.0 - angle_degrees

    return {
        "opposite": opposite,
        "adjacent": adjacent,
        "hypotenuse": hypotenuse,
        "angle_degrees": angle_degrees,
        "other_angle_degrees": other_angle_degrees,
    }