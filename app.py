import json
import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NJMVC Written Test Prep", page_icon="🚗", layout="centered"
)


# Load questions dynamically from the external JSON file
@st.cache_data
def load_question_pool():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback if json file is missing
        return [
            {
                "question": (
                    "What is the New Jersey speed limit in business or"
                    " residential districts?"
                ),
                "options": ["20 mph", "25 mph", "30 mph", "35 mph"],
                "answer": "25 mph",
                "explanation": (
                    "Default speed limit in business/residential districts is"
                    " 25 mph."
                ),
            }
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
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []


def reset_quiz():
    st.session_state.score = 0
    st.session_state.current_q_index = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_finished = False

    # Pull 10 random questions from the dynamic pool
    question_pool = load_question_pool()
    st.session_state.selected_questions = random.sample(
        question_pool, min(10, len(question_pool))
    )
    st.session_state.quiz_started = True


# App Header
st.title("🚗 NJMVC Written Test Prep App")
st.markdown(
    "Practice your knowledge with questions loaded dynamically from an external"
    " database!"
)

# Start / Home Screen
if not st.session_state.quiz_started:
    pool_size = len(load_question_pool())
    st.info(
        f"Loaded {pool_size} questions from database. Click below to start a"
        " randomized quiz!"
    )
    if st.button("Start Practice Quiz", type="primary"):
        reset_quiz()
        st.rerun()

elif st.session_state.quiz_finished:
    # Quiz Completed Screen
    st.balloons()
    st.subheader("🎉 Quiz Completed!")
    final_score = st.session_state.score
    total_q = len(st.session_state.selected_questions)
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
            "Keep practicing! Review the New Jersey Driver Manual for sections"
            " you missed."
        )

    if st.button("Try Again (New Questions)"):
        reset_quiz()
        st.rerun()

else:
    # Quiz Layout
    questions = st.session_state.selected_questions
    idx = st.session_state.current_q_index

    # Progress bar and score
    progress = idx / len(questions)
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
                    st.session_state.quiz_finished = True
                    st.rerun()
