from utils.llm import ask_llm

def optimize_resume(resume_text, job_description, missing_skills):
    prompt = f"""
    You are an expert recruiter and resume writer.

    Candidate Resume:
    {resume_text}

    Target Job Description:
    {job_description}

    Missing Skills:
    {missing_skills}

    Provide:
    1. ATS optimization suggestions.
    2. Resume improvement suggestions.
    3. Missing Keywords.
    4. Improved resume bullet examples

    Return a professional report.
"""
    return ask_llm(prompt)