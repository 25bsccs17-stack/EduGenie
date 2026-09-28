import streamlit as st

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 EduGenie")
st.subheader("AI-Powered Educational Platform")

st.write(
    "A personalized learning platform designed to support "
    "students through learning, examination preparation, "
    "assessment, practical understanding, and study planning."
)

st.divider()

mode = st.selectbox(
    "Select a Learning Mode",
    [
        "Learn Mode",
        "Exam Preparation",
        "Quiz Generator",
        "Real-Life Examples",
        "Study Planner"
    ]
)

if mode == "Learn Mode":
    st.header("📚 Learn Mode")
    st.write("Explore structured and comprehensive learning content.")

elif mode == "Exam Preparation":
    st.header("📝 Exam Preparation")
    st.write("Prepare using 2-mark, 5-mark, and 10-mark questions.")

elif mode == "Quiz Generator":
    st.header("🧠 Quiz Generator")
    st.write("Test your understanding through topic-based quizzes.")

elif mode == "Real-Life Examples":
    st.header("🌍 Real-Life Examples")
    st.write("Connect theoretical concepts with practical situations.")

elif mode == "Study Planner":
    st.header("📅 Study Planner")
    st.write("Create a personalized study schedule.")
