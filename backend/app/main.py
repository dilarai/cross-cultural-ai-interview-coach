from fastapi import FastAPI, HTTPException
from app.schemas import InterviewRequest, AnswerRequest
from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

client = genai.Client(api_key=api_key)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

country_style = {
    "USA": """
Focus on:
- leadership
- achievements
- impact
""",

    "Japan": """
Focus strongly on:
- teamwork
- collaboration
- humility

Avoid highly individualistic or leadership-focused questions.
""",

    "Germany": """
Focus on:
- technical expertise
- structured thinking
- problem solving
"""
}

@app.post("/interview/start")
def start_interview(request: InterviewRequest):

    try:
        response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are an interview coach.

Generate ONE interview question.

Role:
{request.role}

Country:
{request.country}

IMPORTANT:
The question MUST reflect the interview culture of this country.

Interview style:
{country_style.get(request.country, "")}

Return only the interview question.
"""
)
        

        return {
            "question": response.text.strip()
        }

    except Exception as e:

        print("Gemini error:", repr(e))

        raise HTTPException(
            status_code=500,
            detail="Unable to generate interview question."
        )

@app.post("/interview/answer")
def answer_interview(request: AnswerRequest):

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""
You are an expert interview coach.

Evaluate the following interview answer.

Return ONLY valid JSON.

Rules:
- score must be between 1 and 10
- strengths: maximum 2 items
- weaknesses: maximum 2 items
- improvements: maximum 3 items
- sample_answer must be under 80 words
- be concise
- do not include explanations outside the JSON

Format:

{{
    "score": 1,
    "strengths": ["..."],
    "weaknesses": ["..."],
    "improvements": ["..."],
    "sample_answer": "..."
}}

Answer:
{request.answer}
"""
        )   
        clean_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )
        
        feedback = json.loads(clean_text)
        
        
        return feedback

        

    except Exception as e:
        # log (gerçek projede logging kullanılır)
        print("Gemini error:", repr(e))

        raise HTTPException(
            status_code=500,
            detail="AI service temporarily unavailable"
        )