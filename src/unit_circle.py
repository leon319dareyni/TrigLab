"""Unit-circle visualization."""

import math

import matplotlib.pyplot as plt

def create_unit_circle(angle_degrees: float):
    """Create a Matplotlib figure showing an angle on the unit circle."""
    if not math.isfinite(angle_degrees):
        raise ValueError("Angle must be finite number.")

    angle = math.radians(angle_degrees)
    x = math.cos(angle)
    y = math.sin(angle)

    fig, ax = plt.subplots(figsize=(7,7))

    circle = plt.Circle(
        (0,0),
        1,
        fill=False,
        linewidth=2,
    )

    ax.add_patch(circle)

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)


    ax.plot([0,x],[0,y], linewidth=2)

    ax.scatter([x],[y], s=80, zorder=3)

    ax.annotate(
        f"({x:.3f}, {y:.3f})",
        (x,y),
        xytext=(8,8),
        textcoords="offset points",
    )

    ax.set_title(f"Unit circle of {angle_degrees:g}°")
    ax.set_xlabel("x = cos(θ)")
    ax.set_ylabel("y = sin(θ)")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    return fig

