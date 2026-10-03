import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NJMVC Written Test Prep", page_icon="🚗", layout="centered"
)

# Question Bank
QUESTIONS = [
    {
        "question": (
            "What is the New Jersey speed limit in business or residential"
            " districts, unless otherwise posted?"
        ),
        "options": ["20 mph", "25 mph", "30 mph", "35 mph"],
        "answer": "25 mph",
        "explanation": (
            "In school zones, business, or residential districts, the speed"
            " limit is 25 mph unless otherwise posted."
        ),
    },
    {
        "question": (
            "Under NJ law, a motorist who refuses to take a breath test is subject"
            " to an MVC insurance surcharge of how much per year for 3 years?"
        ),
        "options": ["$500", "$1,000", "$1,500", "$2,000"],
        "answer": "$1,000",
        "explanation": (
            "Refusal to take a breath test in NJ results in a MVC insurance"
            " surcharge of $1,000 per year for three years, along with the loss"
            " of driving privileges."
        ),
    },
    {
        "question": (
            "What should you do if your wheels drift onto the dirt shoulder of"
            " the road and you want to return to the paved road?"
        ),
        "options": [
            "Slam on the brakes immediately and turn sharply.",
            "Slow down, regain control, and slowly turn back onto the pavement.",
            (
                "Speed up to match traffic and jerk the steering wheel to the"
                " left."
            ),
            "Shift into neutral and pull over completely.",
        ],
        "answer": (
            "Slow down, regain control, and slowly turn back onto the pavement."
        ),
        "explanation": (
            "If your wheels drift off the road, stay calm, ease up on the gas,"
            " slow down, and slowly steer back onto the pavement when it is"
            " safe."
        ),
    },
    {
        "question": (
            "You are parked on a downhill street with a curb facing the right."
            " In which direction should you turn your wheels?"
        ),
        "options": [
            "Away from the curb (to the left)",
            "Toward the curb (to the right)",
            "Straight ahead",
            "It doesn't matter",
        ],
        "answer": "Toward the curb (to the right)",
        "explanation": (
            "When parking downhill with a curb, your vehicle's front wheels"
            " should be turned sharply toward the curb so the vehicle rolls"
            " against the curb if brakes fail."
        ),
    },
    {
        "question": (
            "In New Jersey, what blood alcohol concentration (BAC) is considered"
            " legal intoxication for drivers 21 years of age or older?"
        ),
        "options": ["0.02%", "0.05%", "0.08%", "0.10%"],
        "answer": "0.08%",
        "explanation": (
            "For drivers age 21 and older, it is illegal to drive with a BAC"
            " of 0.08% or higher. For drivers under 21, any detectable amount"
            " (0.01% or higher) violates zero-tolerance laws."
        ),
    },
    {
        "question": (
            "What is the shape of a yield sign?"
        ),
        "options": [
            "Octagon",
            "Triangle",
            "Diamond",
            "Rectangle",
        ],
        "answer": "Triangle",
        "explanation": (
            "A yield sign is a red and white equilateral triangle. It means you"
            " must slow down and give way to traffic on the roadway you are"
            " entering or crossing."
        ),
    },
    {
        "question": (
            "Unless otherwise posted, the speed limit on certain state highways"
            " and interstates is:"
        ),
        "options": ["45 mph", "50 mph", "55 mph", "65 mph"],
        "answer": "55 mph",
        "explanation": (
            "Certain state highways and all interstates have a default speed"
            " limit of 55 mph unless posted otherwise (though some designated"
            " highways allow up to 65 mph)."
        ),
    },
    {
        "question": (
            "To safely share the road with large trucks and buses, you must"
            " know:"
        ),
        "options": [
            (
                "That they can stop in the same distance as a passenger"
                " vehicle."
            ),
            (
                "The limitations of these vehicles regarding visibility,"
                " required stopping distance, and maneuverability."
            ),
            "That they have the right-of-way at all intersections.",
            "That they cannot make wide right turns.",
        ],
        "answer": (
            "The limitations of these vehicles regarding visibility,"
            " required stopping distance, and maneuverability."
        ),
        "explanation": (
            "Large vehicles have blind spots (no-zones), require significantly"
            " more stopping distance, and make wide turns. Drivers must give"
            " them extra room."
        ),
    },
    {
        "question": (
            "If a school bus has stopped directly in front of a school to pick"
            " up or let off children, a motorist may pass from either direction"
            " at a speed of no more than:"
        ),
        "options": ["10 mph", "15 mph", "20 mph", "25 mph"],
        "answer": "10 mph",
        "explanation": (
            "If a school bus is parked directly in front of a school to let off"
            " or pick up children, you may pass at a speed of no more than 10"
            " mph."
        ),
    },
    {
        "question": (
            "Headlights must be used:"
        ),
        "options": [
            "Only between midnight and sunrise.",
            (
                "One-half hour after sunset to one-half hour before sunrise,"
                " and anytime visibility is 500 feet or less."
            ),
            "Only when it is actively raining or snowing.",
            "Whenever you are driving on a highway.",
        ],
        "answer": (
            "One-half hour after sunset to one-half hour before sunrise, and"
            " anytime visibility is 500 feet or less."
        ),
        "explanation": (
            "NJ law requires headlights to be on half an hour after sunset to"
            " half an hour before sunrise, when using windshield wipers (during"
            " rain, snow, ice), or when visibility is reduced below 500 feet."
        ),
    },
]

# Initialize Session State Variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_q_index" not in st.session_state:
    st.session_state.current_q_index = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_option" not in st.session_state:
    st.session_state.selected_option = None
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = QUESTIONS.copy()


def reset_quiz():
    st.session_state.score = 0
    st.session_state.current_q_index = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    random.shuffle(st.session_state.shuffled_questions)
    st.session_state.quiz_started = True


# App Header
st.title("🚗 NJMVC Written Test Prep App")
st.markdown("Practice your knowledge of New Jersey traffic laws and road rules.")

# Start / Home Screen
if not st.session_state.quiz_started:
    st.info(
        "Click the button below to start a practice quiz session with questions"
        " modeled after the NJ Driver Manual."
    )
    if st.button("Start Practice Quiz", type="primary"):
        reset_quiz()
        st.rerun()

else:
    # Quiz Layout
    questions = st.session_state.shuffled_questions
    idx = st.session_state.current_q_index

    # Progress bar and score
    progress = (idx) / len(questions)
    st.progress(progress)
    st.write(f"**Question {idx + 1} of {len(questions)}**")
    st.write(f"Current Score: {st.session_state.score}")

    st.markdown("---")

    current_question = questions[idx]
    st.subheader(current_question["question"])

    # Radio button for options
    selected = st.radio(
        "Select your answer:",
        current_question["options"],
        key=f"q_{idx}",
        index=(
            current_question["options"].index(st.session_state.selected_option)
            if st.session_state.selected_option in current_question["options"]
            else 0
        ),
        disabled=st.session_state.answered,
    )

    st.session_state.selected_option = selected

    col1, col2 = st.columns(2)

    with col1:
        if not st.session_state.answered:
            if st.button("Submit Answer", type="primary"):
                st.session_state.answered = True
                if (
                    st.session_state.selected_option
                    == current_question["answer"]
                ):
                    st.session_state.score += 1
                st.rerun()

    # Feedback and Explanation display
    if st.session_state.answered:
        if st.session_state.selected_option == current_question["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(
                f"❌ Incorrect. The correct answer is:"
                f" **{current_question['answer']}**"
            )

        st.info(f"**Explanation:** {current_question['explanation']}")

        with col2:
            if idx < len(questions) - 1:
                if st.button("Next Question ➡️"):
                    st.session_state.current_q_index += 1
                    st.session_state.answered = False
                    st.session_state.selected_option = None
                    st.rerun()
            else:
                if st.button("View Final Results 🏆"):
                    st.session_state.current_q_index += (
                        1  # Move past last index to show results screen
                    )
                    st.rerun()

    # Quiz Completed Screen
    if st.session_state.current_q_index >= len(questions):
        st.empty()
        st.balloons()
        st.subheader("🎉 Quiz Completed!")
        final_score = st.session_state.score
        total_q = len(questions)
        percentage = (final_score / total_q) * 100

        st.write(
            f"You scored **{final_score} out of {total_q}** ({percentage:.0f}%)"
        )

        if percentage >= 80:
            st.success(
                "Great job! You are showing a strong understanding of NJMVC"
                " rules."
            )
        else:
            st.warning(
                "Keep practicing! Review the New Jersey Driver Manual for"
                " sections you missed."
            )

        if st.button("Try Again"):
            reset_quiz()
            st.rerun()
