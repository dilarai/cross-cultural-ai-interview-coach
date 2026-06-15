from pydantic import BaseModel

class InterviewRequest(BaseModel):
    role: str
    country: str

class AnswerRequest(BaseModel):
    answer: str

class AnswerRequest(BaseModel):
    answer: str

class FeedbackResponse(BaseModel):
    score: int
    strengths: list[str]
    weaknesses: list[str]
    improvements: list[str]
    sample_answer: str

class NextQuestionRequest(BaseModel):
    session_id: str