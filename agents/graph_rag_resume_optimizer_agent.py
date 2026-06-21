from vector_db.retriever import retrieve_context
from utils.llmgroq_client import llm

def graph_rag_resume_optimizer_agent(state):
    resume_text = state["resume_text"]
    job_description = state["job_description"]

    query = f"""
    Resume Optimization Guidelines

    Job Description: {job_description}

    Resume: {resume_text}

    """

    rag_context = retrieve_context(query=query,k=5)
    prompt = f"""
    You are an expert ATS Resume Reviewer.
    Use the retrieved knowledge base context below.

    Retrieved Context: {rag_context}
    Candidate Resume: {resume_text}
    Target Job Description: {job_description}

    Tasks:
    1. Identify ATS issues.
    2. Identify missing keywords.
    3. Suggest improvements.
    4. Rewrite weak resume bullets.
    5. Improve ATS compatibility.

    Return a detailed optimized resume report.

"""
    response = llm.invoke(prompt)
    state['optimized_resume'] = response.content
    return state