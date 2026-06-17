from utils.llm import ask_llm

def generate_cover_letter(resume_data,job_description):
    prompt = f"""
    You are professional career coach.

    Using the candidate profile and job description, generate a tailored cover letter.

    Candidate Profile:
    {resume_data}

    Job Description:
    {job_description}

    Requirements:
    1. Professional Tone.
    2. 300-400 words.
    3. Highlight relevant skills.
    4. Explain why the candidate is a good fit.
    5. End with a strong closing paragraph.
"""
    return ask_llm(prompt)