from openai import OpenAI
from app.config import OPENAI_MODEL
from .base import BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(self):
        self.client = OpenAI()

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content
        if content is None:
            return ""
        return content
