# EduGenie – Installation Guide

## 1. Prerequisites

Install the following software:

- Python
- Visual Studio Code
- Google AI Studio account

## 2. Create the Project

Create a folder named:

EduGenie

Open the folder in Visual Studio Code.

## 3. Create a Virtual Environment

Open the VS Code terminal and run:

python -m venv venv

Activate the virtual environment:

venv\Scripts\activate

## 4. Install Required Packages

Run:

pip install streamlit google-genai python-dotenv

## 5. Configure Gemini API

Create a `.env` file in the project folder.

Add:

GEMINI_API_KEY=your_api_key_here

Replace `your_api_key_here` with your own Gemini API key.

Do not share the API key or upload the `.env` file to GitHub.

## 6. Run the Application

In the VS Code terminal, run:

streamlit run app.py

The EduGenie application will open in the web browser.

## 7. Stop the Application

To stop the Streamlit application, return to the terminal and press:

Ctrl + C

## 8. Troubleshooting

### API Key Error

Make sure the `.env` file exists and contains the Gemini API key.

### API Quota Error

If a 429 quota or rate-limit error appears, wait until the Gemini API limit becomes available again.

### Missing Package Error

Run:

pip install streamlit google-genai python-dotenv