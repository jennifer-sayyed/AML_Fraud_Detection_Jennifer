from pydantic import BaseModel
from typing import List


class ChatResponse(BaseModel):

    intent: str

    answer: str

    confidence: float

    risk_score: int

    fraud_probability: float

    recommendation: str

    alerts: List[str]

    reasoning_summary: str