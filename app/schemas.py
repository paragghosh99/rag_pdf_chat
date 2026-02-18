from pydantic import BaseModel

class IngestRequest(BaseModel):
    pdf_path: str


class QuestionRequest(BaseModel):
    question: str