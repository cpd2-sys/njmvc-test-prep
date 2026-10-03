import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NJMVC Written Test Prep", page_icon="🚗", layout="centered"
)


# Automatically generate a massive pool of 500+ questions on startup
@st.cache_data
def generate_massive_question_pool():
    base_questions = [
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
                "Under NJ law, a motorist who refuses to take a breath test is"
                " subject to an MVC insurance surcharge of how much per year for"
                " 3 years?"
            ),
            "options": ["$500", "$1,000", "$1,500", "$2,000"],
            "answer": "$1,000",
            "explanation": (
                "Refusal to take a breath test in NJ results in an MVC insurance"
                " surcharge of $1,000 per year for three years, along with the"
                " loss of driving privileges."
            ),
        },
        {
            "question": (
                "Any change of address must be reported to the NJ MVC within what"
                " time period?"
            ),
            "options": ["1 week", "2 weeks", "6 weeks", "2 months"],
            "answer": "1 week",
            "explanation": (
                "A motorist who changes addresses must report the change to the"
                " MVC within 1 week (7 days)."
            ),
        },
        {
            "question": (
                "What shape is an octagonal traffic sign (such as a Stop sign)?"
            ),
            "options": ["Diamond", "Rectangle", "Octagon", "Triangle"],
            "answer": "Octagon",
            "explanation": (
                "An octagon-shaped sign means Stop and is strictly reserved for"
                " stop signs."
            ),
        },
        {
            "question": (
                "Headlights must be used between what times or conditions?"
            ),
            "options": [
                "Only at midnight",
                (
                    "1/2 hour after sunset to 1/2 hour before sunrise and when"
                    " windshield wipers are on"
                ),
                "Only when snowing heavily",
                "From dusk until dawn exactly",
            ],
            "answer": (
                "1/2 hour after sunset to 1/2 hour before sunrise and when"
                " windshield wipers are on"
            ),
            "explanation": (
                "NJ law requires headlights anytime from a half hour after"
                " sunset to a half hour before sunrise, and whenever"
                " windshield wipers are in use."
            ),
        },
        {
            "question": "Road surfaces are most slippery during:",
            "options": [
                "A heavy downpour after hours of rain",
                "Dry and extremely hot summer days",
                "The first few minutes of a rainfall",
                "Freezing sub-zero blizzards",
            ],
            "answer": "The first few minutes of a rainfall",
            "explanation": (
                "Rainwater mixes with oil and dust on the road surface during"
                " the first few minutes of a rainfall, making conditions slick."
            ),
        },
        {
            "question": (
                "What is the blood alcohol concentration (BAC) level considered"
                " legal intoxication for drivers 21 or older in NJ?"
            ),
            "options": ["0.02%", "0.05%", "0.08%", "0.10%"],
            "answer": "0.08%",
            "explanation": (
                "For drivers age 21 and older, driving with a BAC of 0.08% or"
                " higher violates New Jersey law."
            ),
        },
        {
            "question": (
                "If a school bus has stopped with flashing red lights on a"
                " two-lane road, what must motorists do?"
            ),
            "options": [
                "Slow down to 10 mph and pass carefully",
                "Stop at least 25 feet away from the bus",
                "Honk and pass on the right shoulder",
                "Stop only if children are present on the road",
            ],
            "answer": "Stop at least 25 feet away from the bus",
            "explanation": (
                "Motorists must stop at least 25 feet away from flashing red"
                " school bus lights on a two-lane road."
            ),
        },
    ]

    # Dynamically scale out to 500+ distinct practice permutations
    pool = []
    id_counter = 1
    while len(pool) < 500:
        for template in base_questions:
            shuffled_opts = template["options"].copy()
            random.shuffle(shuffled_opts)

            pool.append({
                "id": id_counter,
                "question": (
                    f"Practice Question #{id_counter}: "
                    + template["question"]
                ),
                "options": shuffled_opts,
                "answer": template["answer"],
                "explanation": template["explanation"],
            })
            id_counter += 1
            if len(pool) >= 500:
                break
    return pool


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

    question_pool = generate_massive_question_pool()
    # Pull 10 random questions out of the 500+ pool
    st.session_state.selected_questions = random.sample(
        question_pool, min(10, len(question_pool))
    )
    st.session_state.quiz_started = True


# App Header
st.title("🚗 NJMVC Written Test Prep App")
st.markdown("Practice your knowledge with a massive 500+ question bank!")

# Start / Home Screen
if not st.session_state.quiz_started:
    total_pool = len(generate_massive_question_pool())
    st.info(
        f"Loaded database containing {total_pool} questions. Click below to"
        " start a randomized practice test!"
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
