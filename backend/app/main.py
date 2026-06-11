from fastapi import FastAPI, HTTPException
from app.schemas import InterviewRequest, AnswerRequest
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client(api_key=api_key)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/interview/start")
def start_interview(request: InterviewRequest):
    return {
        "role": request.role,
        "country": request.country,
        "question": "Tell me about yourself."
    }


@app.post("/interview/answer")
def answer_interview(request: AnswerRequest):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are an interview coach.

Evaluate the following answer clearly and professionally.

Answer:
{request.answer}
"""
        )

        return {
            "feedback": response.text
        }

    except Exception as e:
        # log (gerçek projede logging kullanılır)
        print("Gemini error:", repr(e))

        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )