from fastapi import FastAPI
from app.schemas import InterviewRequest, AnswerRequest

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

@app.post("/interview/answer")
def answer_interview(request: AnswerRequest):
    return {
        "feedback": "Good answer."
    }
