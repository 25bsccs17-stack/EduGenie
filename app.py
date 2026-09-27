import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Page settings
st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="wide"
)

# Check API key
if not API_KEY:
    st.error("Gemini API key was not found. Please create a .env file.")
    st.stop()

# Gemini client
client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash-lite"

# -------------------------------
# HEADER
# -------------------------------

st.title("🎓 EduGenie")
st.subheader("Your Gemini-Powered Personal Learning Assistant")

st.write(
    "EduGenie helps students learn topics, prepare for exams, "
    "generate quizzes, understand real-life examples, and create study plans."
)

st.divider()

# -------------------------------
# SIDEBAR
# -------------------------------

st.sidebar.title("📚 Learning Modes")

mode = st.sidebar.selectbox(
    "Choose a mode",
    [
        "Learn",
        "Exam Preparation",
        "Quiz Generator",
        "Real-Life Examples",
        "Study Planner"
    ]
)

st.sidebar.info(
    "EduGenie uses Google Gemini to generate personalized educational content."
)

# -------------------------------
# TOPIC
# -------------------------------

topic = st.text_input(
    "📖 Enter your topic",
    placeholder="Example: Java Inheritance"
)

# -------------------------------
# STUDY PLANNER INPUT
# -------------------------------

days = 7
hours = 2

if mode == "Study Planner":

    days = st.number_input(
        "Number of study days",
        min_value=1,
        max_value=60,
        value=7
    )

    hours = st.number_input(
        "Study hours per day",
        min_value=1,
        max_value=12,
        value=2
    )

# -------------------------------
# GENERATE
# -------------------------------

if st.button("✨ Generate", use_container_width=True):

    if not topic.strip():

        st.warning("Please enter a topic first.")

    else:

        # Learn mode
        if mode == "Learn":

            prompt = f"""
You are EduGenie, a friendly educational AI assistant.

Teach the student about:

{topic}

Assume the student is a beginner.

Provide:

1. Simple definition
2. Easy explanation
3. Important concepts
4. Real-life example
5. Simple example
6. Quick revision points

Use clear and student-friendly language.
"""

        # Exam mode
        elif mode == "Exam Preparation":

            prompt = f"""
You are EduGenie, an exam preparation assistant.

Topic:

{topic}

Create exam-oriented study material.

Include:

1. Definition
2. Introduction
3. Important points
4. Detailed explanation
5. Example
6. Applications
7. Conclusion

Then provide:

2-mark answer
5-mark answer
10-mark answer

Use clear college-level language.
"""

        # Quiz mode
        elif mode == "Quiz Generator":

            prompt = f"""
You are EduGenie, an educational quiz generator.

Create a quiz about:

{topic}

Generate 5 multiple-choice questions.

For each question provide:

Question
A
B
C
D
Correct Answer
Short Explanation

Make the questions suitable for a college student.
"""

        # Examples mode
        elif mode == "Real-Life Examples":

            prompt = f"""
You are EduGenie.

Explain the topic:

{topic}

using real-world examples.

Provide:

1. Simple explanation
2. Three real-life examples
3. Explanation of each example
4. One easy analogy
5. Quick summary

Use simple student-friendly language.
"""

        # Study planner
        elif mode == "Study Planner":

            prompt = f"""
You are EduGenie, a smart study planning assistant.

Create a practical study plan.

Topic:
{topic}

Number of days:
{days}

Study hours per day:
{hours}

For every day provide:

Day
Topic/Subtopic
Study Activity
Revision Activity
Practice Activity

Make the plan realistic for a college student.
"""

        # -------------------------------
        # CALL GEMINI
        # -------------------------------

        with st.spinner("🤖 EduGenie is generating your content..."):

            try:

                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=prompt
                )

                st.success("Content generated successfully!")

                st.subheader("📚 EduGenie Result")

                st.markdown(response.text)

            except Exception as error:

                st.error("Unable to generate the response.")

                st.write("Error details:")
                st.code(str(error))

# -------------------------------
# FOOTER
# -------------------------------

st.divider()

st.caption(
    "EduGenie | Gemini Powered Learning Assistant | Academic Project"
)