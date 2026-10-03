import random
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="NJMVC Written Test Prep", page_icon="🚗", layout="centered"
)


@st.cache_data
def get_unique_question_pool():
    return [
        {
            "id": 1,
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
            "id": 2,
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
            "id": 3,
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
            "id": 4,
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
            "id": 5,
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
            "id": 6,
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
            "id": 7,
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
            "id": 8,
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
        {
            "id": 9,
            "question": (
                "What should you do if your wheels drift onto the dirt shoulder"
                " of the road and you want to return to the paved road?"
            ),
            "options": [
                "Slam on the brakes immediately and turn sharply.",
                (
                    "Slow down, regain control, and slowly turn back onto the"
                    " pavement."
                ),
                (
                    "Speed up to match traffic and jerk the steering wheel to"
                    " the left."
                ),
                "Shift into neutral and pull over completely.",
            ],
            "answer": (
                "Slow down, regain control, and slowly turn back onto the"
                " pavement."
            ),
            "explanation": (
                "If your wheels drift off the road, stay calm, ease up on the"
                " gas, slow down, and slowly steer back onto the pavement when"
                " it is safe."
            ),
        },
        {
            "id": 10,
            "question": (
                "You are parked on a downhill street with a curb facing the"
                " right. In which direction should you turn your wheels?"
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
            "id": 11,
            "question": "What is the shape of a yield sign?",
            "options": ["Octagon", "Triangle", "Diamond", "Rectangle"],
            "answer": "Triangle",
            "explanation": (
                "A yield sign is a red and white equilateral triangle. It means"
                " you must slow down and give way to traffic on the roadway you"
                " are entering or crossing."
            ),
        },
        {
            "id": 12,
            "question": (
                "Unless otherwise posted, the speed limit on certain state"
                " highways and interstates is:"
            ),
            "options": ["45 mph", "50 mph", "55 mph", "65 mph"],
            "answer": "55 mph",
            "explanation": (
                "Certain state highways and all interstates have a default"
                " speed limit of 55 mph unless posted otherwise."
            ),
        },
        {
            "id": 13,
            "question": (
                "To safely share the road with large trucks and buses, you"
                " must know:"
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
                "Large vehicles have blind spots (no-zones), require"
                " significantly more stopping distance, and make wide turns."
            ),
        },
        {
            "id": 14,
            "question": (
                "During bad weather conditions, how much longer does a truck"
                " take to stop?"
            ),
            "options": [
                "It takes the same distance as a car.",
                "25% more",
                "50% more",
                "Up to 25% more",
            ],
            "answer": "Up to 25% more",
            "explanation": (
                "Under adverse weather conditions, a truck can take as much as"
                " 25% longer to stop than under normal conditions."
            ),
        },
        {
            "id": 15,
            "question": (
                "What should you do if your brakes suddenly fail while driving?"
            ),
            "options": [
                "Jump out of the car immediately.",
                (
                    "Shift to a lower gear and pump the brake pedal hard and"
                    " fast several times."
                ),
                "Turn off the ignition key instantly.",
                (
                    "Pull the emergency brake all the way up immediately at"
                    " high speed."
                ),
            ],
            "answer": (
                "Shift to a lower gear and pump the brake pedal hard and fast"
                " several times."
            ),
            "explanation": (
                "If brakes fail, shift to a lower gear and pump the brake pedal"
                " fast and hard."
            ),
        },
        {
            "id": 16,
            "question": (
                "What is the penalty for altering a driver license or showing"
                " an altered driver license?"
            ),
            "options": [
                "A fine of up to $200",
                (
                    "A fine of up to $1,000, up to 6 months imprisonment, and"
                    " loss of driving privilege"
                ),
                "A warning letter from the MVC",
                "Only a 30-day suspension",
            ],
            "answer": (
                "A fine of up to $1,000, up to 6 months imprisonment, and loss"
                " of driving privilege"
            ),
            "explanation": (
                "Alteration of a license or showing an altered license can"
                " result in a fine up to $1,000, imprisonment up to 6 months,"
                " and loss of driving privileges."
            ),
        },
        {
            "id": 17,
            "question": (
                "Except when parking, what is the rule for cell phone use while"
                " driving for a holder of a GDL permit or license?"
            ),
            "options": [
                "Allowed using a hands-free device only.",
                "Allowed for emergency calls only.",
                (
                    "Strictly prohibited (no hand-held or hands-free cellular"
                    " devices)."
                ),
                "Allowed if talking to parents.",
            ],
            "answer": (
                "Strictly prohibited (no hand-held or hands-free cellular"
                " devices)."
            ),
            "explanation": (
                "GDL drivers (permit or probationary holders) may not use any"
                " electronic devices, hand-held or hands-free, while driving."
            ),
        },
        {
            "id": 18,
            "question": "What color is a rectangular regulatory sign?",
            "options": [
                "Yellow and black",
                "White and red, or black and white",
                "Green and white",
                "Orange and black",
            ],
            "answer": "White and red, or black and white",
            "explanation": (
                "Regulatory signs convey rules like speed limits or stop rules"
                " and are typically black and white or red and white."
            ),
        },
        {
            "id": 19,
            "question": (
                "When approaching an uncontrolled intersection, what is the best"
                " practice?"
            ),
            "options": [
                "Speed up to clear the intersection quickly.",
                (
                    "Reduce speed and be ready to stop if any traffic is coming"
                    " from the right or left."
                ),
                "Always assume you have the right-of-way.",
                "Close your eyes and cross.",
            ],
            "answer": (
                "Reduce speed and be ready to stop if any traffic is coming from"
                " the right or left."
            ),
            "explanation": (
                "An uncontrolled intersection means no signs or signals are"
                " present. You should reduce speed and be prepared to yield."
            ),
        },
        {
            "id": 20,
            "question": (
                "In New Jersey, drivers are subject to double fines for motor"
                " vehicle violations committed in:"
            ),
            "options": [
                "School zones",
                "Construction or work zones",
                "Residential zones",
                "Hospital zones",
            ],
            "answer": "Construction or work zones",
            "explanation": (
                "Fines are doubled for various motor vehicle violations"
                " committed within designated safe corridors or"
                " construction/work zones."
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
if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []

# Track consecutive correct streaks per question ID (e.g., {q_id: streak_count})
if "mastery_streaks" not in st.session_state:
    st.session_state.mastery_streaks = {}


def reset_quiz():
    st.session_state.score = 0
    st.session_state.current_q_index = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_finished = False

    all_pool = get_unique_question_pool()

    # Filter out questions that have been mastered (streak >= 2)
    # If all questions are mastered, reset streaks so user can keep studying!
    available_pool = [
        q
        for q in all_pool
        if st.session_state.mastery_streaks.get(q["id"], 0) < 2
    ]

    if not available_pool:
        st.session_state.mastery_streaks = {}
        available_pool = all_pool

    # Pick up to 10 questions from what's left
    sample_size = min(10, len(available_pool))
    st.session_state.selected_questions = random.sample(
        available_pool, sample_size
    )
    st.session_state.quiz_started = True


# App Header
st.title("🚗 NJMVC Written Test Prep App")
st.markdown(
    "Smart Study Mode: Questions you answer correctly **twice in a row** are"
    " automatically mastered and hidden!"
)

# Show current mastery progress in sidebar/top
mastered_count = sum(
    1 for q_id, streak in st.session_state.mastery_streaks.items() if streak >= 2
)
total_questions = len(get_unique_question_pool())
st.sidebar.metric(
    label="🧠 Mastered Questions", value=f"{mastered_count} / {total_questions}"
)

if st.sidebar.button("Reset Mastery Progress"):
    st.session_state.mastery_streaks = {}
    st.rerun()

# Start / Home Screen
if not st.session_state.quiz_started:
    st.info(
        "Click below to start a smart practice session focusing on unmastered"
        " material!"
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
            "Great job! Mastered questions have been removed from your next"
            " round."
        )
    else:
        st.warning(
            "Keep practicing! Review the New Jersey Driver Manual for sections"
            " you missed."
        )

    if st.button("Start Next Round (Smart Filtered)"):
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
    q_id = current_question["id"]

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
                is_correct = (
                    st.session_state.selected_option
                    == current_question["answer"]
                )

                if is_correct:
                    st.session_state.score += 1
                    # Increase streak for this specific question ID
                    st.session_state.mastery_streaks[q_id] = (
                        st.session_state.mastery_streaks.get(q_id, 0) + 1
                    )
                else:
                    # Reset streak to 0 if answered incorrectly
                    st.session_state.mastery_streaks[q_id] = 0

                st.rerun()

    # Feedback and Explanation display
    if st.session_state.answered:
        if st.session_state.selected_option == current_question["answer"]:
            st.success("✅ Correct!")
            current_streak = st.session_state.mastery_streaks.get(q_id, 0)
            if current_streak >= 2:
                st.balloons()
                st.info(
                    "⭐ **Mastery Achieved!** You've answered this question"
                    " correctly twice in a row. It will be omitted from future"
                    " sets!"
                )
            else:
                st.info(
                    f"🔥 Mastery Streak: {current_streak}/2 correct"
                    " consecutive times."
                )
        else:
            st.error(
                f"❌ Incorrect. The correct answer is:"
                f" **{current_question['answer']}**"
            )
            st.warning("⚠️ Streak reset to 0. You'll see this question again.")

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
