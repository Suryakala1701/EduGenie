from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import Optional

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# Allow frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = genai.GenerativeModel("gemini-3.8-flash")

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "EduGenie backend is running"}

@app.post("/ask")
def ask_question(data: Question):
    response = model.generate_content(data.question)
    return {"answer": response.text}

class QuizRequest(BaseModel):
    topic: str

@app.post("/generate-quiz")
def generate_quiz(data: QuizRequest):
    prompt = f"""Create a 5-question multiple choice quiz on the topic: {data.topic}.
    For each question, give 4 options labeled A, B, C, D, and clearly state the correct answer at the end.
    Keep it clear and well formatted."""
    response = model.generate_content(prompt)
    return {"quiz": response.text}


class RecommendRequest(BaseModel):
    topic: str

@app.post("/recommend")
def recommend_path(data: RecommendRequest):
    prompt = f"""Create a structured beginner-to-advanced learning path for: {data.topic}.
    Include stages, what to learn in each stage, and a rough timeline."""
    response = model.generate_content(prompt)
    return {"learning_path": response.text}


class SummarizeRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: SummarizeRequest):
    prompt = f"Summarize the following text in a clear, concise way:\n\n{data.text}"
    response = model.generate_content(prompt)
    return {"summary": response.text}