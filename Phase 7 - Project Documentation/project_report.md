# EduGenie – Project Report

## 1. Introduction

EduGenie is a Google Gemini-powered personal learning assistant designed to help students learn educational topics in a simple and interactive way.

The application uses artificial intelligence to generate personalized educational content based on the student's selected learning mode and topic.

## 2. Problem Statement

Students often face difficulties understanding complex topics, preparing for examinations, practicing questions, and creating effective study plans.

EduGenie provides an AI-based solution that combines these learning activities in one application.

## 3. Objectives

The main objectives of EduGenie are:

- Help students understand educational topics.
- Provide exam-oriented study material.
- Generate practice quizzes.
- Explain concepts using real-life examples.
- Create personalized study plans.
- Provide an easy-to-use learning interface.

## 4. Features

EduGenie provides five main learning modes:

1. Learn
2. Exam Preparation
3. Quiz Generator
4. Real-Life Examples
5. Study Planner

## 5. Technologies Used

- Python
- Streamlit
- Google Gemini API
- google-genai
- python-dotenv
- Visual Studio Code

## 6. System Architecture

The user interacts with the Streamlit interface.

The Python application processes the user's selected learning mode and topic, creates an appropriate prompt, and sends it to the Google Gemini API.

Gemini generates the educational response, which is then displayed in the Streamlit application.

## 7. Development Process

The project was developed through the following stages:

1. Brainstorming and Ideation
2. Requirement Analysis
3. Project Design
4. Project Planning
5. Project Development
6. Project Testing
7. Project Documentation
8. Project Demonstration

## 8. Testing

The major learning modes were tested using different educational topics.

The application was tested for:

- Topic learning
- Exam preparation
- Quiz generation
- Real-life examples
- Study planning
- Empty topic validation

## 9. Security

The Gemini API key is stored in an environment file and is not hard-coded in the application source code.

The `.env` file should not be uploaded to GitHub.

## 10. Future Enhancements

Future versions of EduGenie could include:

- Student login and profiles
- Learning progress tracking
- Saved study plans
- More quiz types
- Voice-based learning
- PDF study material support
- Personalized learning history

## 11. Conclusion

EduGenie demonstrates how generative AI can be used to support students in different learning activities.

The project combines Python, Streamlit, and Google Gemini to provide an interactive and personalized learning assistant.