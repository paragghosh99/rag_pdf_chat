from app.config import LLM_BACKEND


def get_llm():
    backend = LLM_BACKEND

    if backend == "local":
        from .local_llm import LocalLLM
        return LocalLLM()

    elif backend == "openai":
        from .openai_llm import OpenAILLM
        return OpenAILLM()

    else:
        raise ValueError(f"Unsupported LLM_BACKEND: {backend}")
