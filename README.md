# EduGenie

An AI-powered learning assistant built with FastAPI and Google Gemini.

## Features
- Ask questions and get clear explanations
- Generate quizzes on any topic
- Get personalized learning path recommendations
- Summarize long text

## Tech Stack
- Backend: Python, FastAPI, Uvicorn
- AI: Google Gemini API
- Frontend: HTML (index.html)

## How to Run
1. Install dependencies:
   py -m pip install fastapi uvicorn google-generativeai python-dotenv
2. Create a `.env` file in the backend folder with your key:
   GEMINI_API_KEY=your_key_here
3. Start the server:
   py -m uvicorn main:app --reload
4. Open http://127.0.0.1:8000/docs to test the API.
