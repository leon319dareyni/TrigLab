"""Core trigonometry labratory."""

import math

def degrees_to_radians(degrees: float) -> float:
    """Convert degrees to radians."""
    if not math.isfinite(degrees):
        raise ValueError("Angle must be a finite number.")

    return math.radians(degrees)

def radians_to_degrees(radians: float) -> float:
    """Convert radians to degrees."""
    if not math.isfinite(radians):
        raise ValueError("Angle must be a finite number.")

    return math.degrees(radians)

def calculate_trig(
    angle: float,
    unit: str = "degrees",
) -> dict[str, float | None]:
    """
    Calculate sine, cosine, and tangent.

    Tangent is None when cosine is effectively zero.
    """
    if not math.isfinite(angle):
        raise ValueError("Angle must be a finite number.")

    if unit not in {"degrees","radians"}:
        raise ValueError("Unit must be 'degrees' or 'radians'.")

    radians = (
        math.radians(angle)
        if unit == "degrees"
        else angle
    )

    sine = math.sin(radians)
    cosine = math.cos(radians)

    tangent = (
        None
        if math.isclose(cosine, 0.0, abs_tol=1e-12)
        else sine / cosine
    )

    return {
        "sin": sine,
        "cos": cosine,
        "tan": tangent,
    }


def inverse_trig(
        value: float,
        function: str = "asin",
)-> float:
    """
    Calculate an inverse trigonometric function.
    
    Returns the angle in degrees
    """

    if not math.isfinite(value):
        raise ValueError("Value must be a finite number.")

    functions = {
        "asin": math.asin,
        "acos": math.acos,
        "atan": math.atan,        
    }

    if function not in functions:
        raise ValueError("Use 'asin', 'acos', or 'atan'.")

    if function in {"asin", "acos"} and not -1 <= value <=1:
        raise ValueError("asin and acos require values from -1 to 1.")

    result_radians = functions[function](value)
    return math.degrees(result_radians)