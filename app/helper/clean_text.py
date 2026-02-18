import re

def clean_text(text: str) -> str:
    #remove excessive whitespace and line breaks
    text = re.sub(r"\s+", " ", text)
    return text.strip()