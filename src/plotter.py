"""Trigonometric function plotting."""

import math

import matplotlib.pyplot as plt
import numpy as np

def create_trig_plot(
    start_degrees: float = -180,
    end_degrees: float = 180,
    show_sine: bool = True,
    show_cosine: bool = True,
    show_tangent: bool = False,
):
    """Create a graph of selected trigonometric functions."""
    if not (
        math.isfinite(start_degrees)
        and math.isfinite(end_degrees)
    ):
        raise ValueError("Plot boundaries must be finite.")

    if start_degrees >= end_degrees:
        raise ValueError("Start angle must be less than end angle.")

    if not any([show_sine, show_cosine, show_tangent]):
        raise ValueError("Select at least one function.")

    degrees = np.linspace(
        start_degrees,
        end_degrees,
        3000,
    )
    radians = np.deg2rad(degrees)

    fig, ax = plt.subplots(figsize=(11, 5))

    if show_sine:
        ax.plot(degrees, np.sin(radians), label="sin(x)")

    if show_cosine:
        ax.plot(degrees, np.cos(radians), label="cos(x)")

    if show_tangent:
        tangent = np.tan(radians)

        # Hide extreme values to avoid drawing misleading
        # lines across tangent's vertical asymptotes.
        tangent[np.abs(np.cos(radians)) < 0.025] = np.nan
        tangent[np.abs(tangent) > 10] = np.nan

        ax.plot(degrees, tangent, label="tan(x)")

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_title("Trigonometric Functions")
    ax.set_xlabel("Angle (degrees)")
    ax.set_ylabel("Function value")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()

    return fig