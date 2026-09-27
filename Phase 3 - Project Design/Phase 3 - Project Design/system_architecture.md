# Phase 3 - System Architecture

## Architecture

The EduGenie system follows a simple flow:

User
  |
  v
Streamlit User Interface
  |
  v
Learning Mode Selection
  |
  v
Python Application
  |
  v
Google Gemini API
  |
  v
AI-Generated Educational Content
  |
  v
Streamlit Interface
  |
  v
User

## Components

### 1. User Interface
Streamlit provides the web interface through which students interact with EduGenie.

### 2. Python Application
Python handles user input, learning-mode selection, prompt creation, and communication with Gemini.

### 3. Google Gemini API
Gemini processes the educational prompt and generates the requested learning content.

### 4. Output
The generated content is displayed to the student through the Streamlit interface.