from vector_db.retriever import retrieve_context
from utils.llm import ask_llm


def graph_rag_resume_optimizer_agent(state):
    resume_text = state["resume_data"]
    job_description = state["job_description"]

    query = f"""
    Resume Optimization Guidelines

    Job Description: {job_description}

    Resume: {resume_text}

    """

    rag_context = retrieve_context(query=query,k=5)
    
    prompt = f"""
You are an expert ATS Resume Reviewer and Resume Writer.

Use ONLY the retrieved context provided below.

Retrieved Context:
{rag_context}

Candidate Resume:
{resume_text}

Target Job Description:
{job_description}

TASK 1:
Create an ATS REVIEW REPORT.

Include:

1. ATS Issues
2. Missing Keywords
3. Resume Weaknesses
4. ATS Improvement Suggestions

------------------------------------------------

TASK 2:
Create a COMPLETE ATS-OPTIMIZED RESUME.

Requirements:

- Professional Summary
- Technical Skills
- Projects
- Experience
- Education

Rules:

- **NEVER invent experience.**
- **NEVER invent projects.**
- **NEVER invent certifications.**
- **NEVER invent achievements.**

NEVER invent:
- email
- linkedin
- github
- phone

If information is unavailable write:"Information not available"

Never add technologies that are not present in candidate resume.

Use ATS-friendly formatting.

Return your answer EXACTLY in this format:

ATS_REPORT:
<ATS report here>

OPTIMIZED_RESUME:
<full optimized resume here>

"""
    print("\nExecuting graph_rag_resume_optimizer_agent")
    print("\nRetrieved Context Length:",len(rag_context))
    response = ask_llm(prompt)
    ats_report = ""
    optimized_resume = ""

    if "OPTIMIZED_RESUME:" in response:
        parts = response.split("OPTIMIZED_RESUME:")
        ats_report = (parts[0].replace("ATS_REPORT:","").strip())
        optimized_resume = parts[1].strip()
    else:
        ats_report = response
        optimized_resume = response
    state['retrieved_context'] = rag_context
    state['optimized_resume'] = optimized_resume
    state['ats_report']=ats_report

    # return {
    #     "retrieved_context":rag_context[:1000],
    #     "optimized_resume":optimized_resume
    # }
    return {"ats_report":ats_report,
            "optimized_resume":optimized_resume}