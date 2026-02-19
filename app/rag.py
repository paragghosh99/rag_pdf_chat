from app.vector_store import get_vector_store
from app.prompts import QA_PROMPT
from app.llm.factory import get_llm
from app.config import TOP_K
from app.helper.clean_text import clean_text


def answer_question(question: str) -> str:
    vector_store = get_vector_store()
    
    #fetch_k is retrieving 10 docs where 4 are being filtered by mmr to prevent semantic redundancy
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
        )

    docs = retriever.invoke(question)

    #debugging + monitoring
    with open("retrieved_chunks.txt", "w", encoding="utf-8") as f:
        for i, doc in enumerate(docs):
            f.write(f"\n--- Chunk {i+1} ---\n\n")
            f.write(clean_text(doc.page_content))
            f.write("\n\n")

    context = "\n\n".join(clean_text(doc.page_content) for doc in docs)

    prompt = QA_PROMPT.format(
        context=context,
        question=question
    )

    # RAG → BaseLLM interface → factory → chosen backend
    llm = get_llm()
    answer = llm.generate(prompt)

    return answer
