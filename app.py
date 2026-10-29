"""TrigLab interactive web application."""

import math

import streamlit as st
import matplotlib.pyplot as plt

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
from src.unit_circle import create_unit_circle
from src.plotter import create_trig_plot
from src.quiz import generate_question, check_answer

st.set_page_config(
    page_title="TrigLab",
    page_icon="🧪",
    layout="wide",
)

st.title("🧪 TrigLab")
st.caption("An interactive laboratory for trigonometry.")
st.markdown(
    "Explore mathematical functions, solve triangles, "
    "visualize the unit circle, and test your knowledge."
)

calculator_tab, triangle_tab, circle_tab, plot_tab, quiz_tab = (
    st.tabs([
        "🧮 Calculator",
        "📐 Triangle Solver",
        "⭕ Unit Circle",
        "📈 Function Plotter",
        "🧠 Quiz",
    ])
)

# --------------------------------------------------
# 1. CALCULATOR
# --------------------------------------------------

with calculator_tab:
    st.header("Trigonometric Calculator")

    angle = st.number_input(
        "Enter an angle",
        value=30.0,
        step=1.0,
        key="calculator_angle",
    )

    unit = st.selectbox(
        "Angle unit",
        ["degrees", "radians"],
        key="calculator_unit",
    )

    if st.button("Calculate", key="calculate_trig"):
        try:
            results = calculate_trig(angle, unit)

            col1, col2, col3 = st.columns(3)

            col1.metric("Sine", f"{results['sin']:.8f}")
            col2.metric("Cosine", f"{results['cos']:.8f}")

            if results["tan"] is None:
                col3.metric("Tangent", "Undefined")
            else:
                col3.metric("Tangent", f"{results['tan']:.8f}")

            radians = (
                degrees_to_radians(angle)
                if unit == "degrees"
                else angle
            )
            degrees = radians_to_degrees(radians)

            st.write(f"**Degrees:** {degrees:.8f}°")
            st.write(f"**Radians:** {radians:.8f}")

        except ValueError as error:
            st.error(str(error))

    st.divider()
    st.subheader("Inverse Trigonometry")

    inverse_function = st.selectbox(
        "Function",
        ["asin", "acos", "atan"],
    )

    inverse_value = st.number_input(
        "Input value",
        value=0.5,
        step=0.1,
        key="inverse_value",
    )

    if st.button("Calculate inverse"):
        try:
            result = inverse_trig(
                inverse_value,
                inverse_function,
            )
            st.success(f"Angle: {result:.8f}°")
        except ValueError as error:
            st.error(str(error))

# --------------------------------------------------
# 2. RIGHT-TRIANGLE SOLVER
# --------------------------------------------------

with triangle_tab:
    st.header("Right-Triangle Solver")
    st.write("Choose the information you already know.")

    solve_mode = st.radio(
        "Calculation method",
        [
            "Angle + hypotenuse",
            "Two legs",
        ],
        horizontal=True,
    )

    if solve_mode == "Angle + hypotenuse":
        angle_input = st.number_input(
            "Acute angle (degrees)",
            min_value=0.1,
            max_value=89.9,
            value=30.0,
        )

        hypotenuse_input = st.number_input(
            "Hypotenuse",
            min_value=0.001,
            value=10.0,
        )

        if st.button("Solve triangle"):
            try:
                result = solve_from_angle_hypotenuse(
                    angle_input,
                    hypotenuse_input,
                )

                st.write(f"Opposite: {result['opposite']:.6f}")
                st.write(f"Adjacent: {result['adjacent']:.6f}")
                st.write(f"Hypotenuse: {result['hypotenuse']:.6f}")
                st.write(f"Other angle: {90 - angle_input:.6f}°")

            except ValueError as error:
                st.error(str(error))

    else:
        opposite_input = st.number_input(
            "Opposite side",
            min_value=0.001,
            value=3.0,
            key="opposite",
        )

        adjacent_input = st.number_input(
            "Adjacent side",
            min_value=0.001,
            value=4.0,
            key="adjacent",
        )

        if st.button("Solve from legs"):
            try:
                result = solve_from_legs(
                    opposite_input,
                    adjacent_input,
                )

                st.write(f"Hypotenuse: {result['hypotenuse']:.6f}")
                st.write(f"First angle: {result['angle_degrees']:.6f}°")
                st.write(
                    "Other angle: "
                    f"{result['other_angle_degrees']:.6f}°"
                )

            except ValueError as error:
                st.error(str(error))

# --------------------------------------------------
# 3. UNIT CIRCLE
# --------------------------------------------------

with circle_tab:
    st.header("Interactive Unit Circle")

    circle_angle = st.slider(
        "Rotate the angle",
        min_value=-360,
        max_value=360,
        value=45,
        step=1,
    )

    st.write(f"Selected angle: **{circle_angle}°**")

    fig = create_unit_circle(circle_angle)
    st.pyplot(fig)
    plt.close(fig)

    radians = math.radians(circle_angle)

    col1, col2 = st.columns(2)
    col1.metric("cos(θ) = x", f"{math.cos(radians):.6f}")
    col2.metric("sin(θ) = y", f"{math.sin(radians):.6f}")

# --------------------------------------------------
# 4. FUNCTION PLOTTER
# --------------------------------------------------

with plot_tab:
    st.header("Trigonometric Function Plotter")

    col1, col2 = st.columns(2)

    with col1:
        start_angle = st.number_input(
            "Start angle (degrees)",
            value=-180.0,
            key="plot_start",
        )

    with col2:
        end_angle = st.number_input(
            "End angle (degrees)",
            value=180.0,
            key="plot_end",
        )

    st.write("Choose which functions to display.")

    show_sine = st.checkbox("Sine", value=True)
    show_cosine = st.checkbox("Cosine", value=True)
    show_tangent = st.checkbox("Tangent", value=False)

    if st.button("Plot functions"):
        try:
            fig = create_trig_plot(
                start_angle,
                end_angle,
                show_sine,
                show_cosine,
                show_tangent,
            )

            st.pyplot(fig)
            plt.close(fig)

        except ValueError as error:
            st.error(str(error))

# --------------------------------------------------
# 5. QUIZ
# --------------------------------------------------

with quiz_tab:
    st.header("Trigonometry Challenge")

    if "quiz_question" not in st.session_state:
        st.session_state.quiz_question = generate_question()
        st.session_state.quiz_score = 0
        st.session_state.quiz_attempts = 0
        st.session_state.quiz_feedback = None

    question = st.session_state.quiz_question

    st.write(
        f"What is **{question['function']}"
        f"({question['angle']}°)**?"
    )

    with st.form("quiz_form"):
        answer_input = st.number_input(
            "Your numerical answer",
            value=0.0,
            step=0.1,
            format="%.6f",
        )

        submitted = st.form_submit_button("Check answer")

    if submitted:
        correct_answer = question["answer"]

        st.session_state.quiz_attempts += 1

        if correct_answer is None:
            st.session_state.quiz_feedback = (
                "undefined",
                "Tangent is undefined at this angle.",
            )

        elif check_answer(answer_input, correct_answer):
            st.session_state.quiz_score += 1
            st.session_state.quiz_feedback = (
                "correct",
                "Correct! Excellent work.",
            )

        else:
            st.session_state.quiz_feedback = (
                "incorrect",
                f"Not quite. The correct value is {correct_answer:.6f}.",
            )

    feedback = st.session_state.quiz_feedback

    if feedback is not None:
        status, message = feedback

        if status == "correct":
            st.success(message)
        elif status == "incorrect":
            st.error(message)
        else:
            st.info(message)

    col1, col2 = st.columns(2)

    col1.metric(
        "Correct answers",
        st.session_state.quiz_score,
    )

    col2.metric(
        "Questions attempted",
        st.session_state.quiz_attempts,
    )

    if st.button("Next question"):
        st.session_state.quiz_question = generate_question()
        st.session_state.quiz_feedback = None
        st.rerun()

    if st.button("Reset quiz"):
        st.session_state.quiz_question = generate_question()
        st.session_state.quiz_score = 0
        st.session_state.quiz_attempts = 0
        st.session_state.quiz_feedback = None
        st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()
st.caption(
    "TrigLab v1.0.0 | Built with Python, NumPy, "
    "Matplotlib, and Streamlit."
)