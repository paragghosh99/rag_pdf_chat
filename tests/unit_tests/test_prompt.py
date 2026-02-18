# tests/test_prompt.py

from app.prompts import QA_PROMPT

def test_prompt_contains_context_and_question():
    context = "AI is artificial intelligence."
    question = "What is AI?"

    prompt = QA_PROMPT.format(context=context, question=question)

    assert context in prompt
    assert question in prompt
    assert "Answer:" in prompt
