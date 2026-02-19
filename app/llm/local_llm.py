from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from app.config import LOCAL_MODEL_NAME as MODEL_NAME
from .base import BaseLLM
from typing import Optional, Any


class LocalLLM(BaseLLM):
    def __init__(self):
        self.tokenizer: Optional[Any] = None
        self.model: Optional[Any] = None

    def _load_model(self):
        if self.model is None:
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    def generate(self, prompt: str) -> str:
        self._load_model()
        assert self.tokenizer is not None
        assert self.model is not None
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        outputs = self.model.generate(**inputs, max_new_tokens=150)

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
