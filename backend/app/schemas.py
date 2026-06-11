from pydantic import BaseModel

class InterviewRequest(BaseModel):
    role: str
    country: str

class AnswerRequest(BaseModel):
    answer: str

class AnswerRequest(BaseModel):
    answer: str