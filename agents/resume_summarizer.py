from utils.llm import ask_llm

def generate_resume_summary(resume_text):
    prompt = f"""
    Summarize this resume professionally.

    Include:
    - Years of experience
    - Core skills
    - Education
    - Major Achievements

    Resume:
    {resume_text}

    Limit to 150 words.

    """

    return ask_llm(prompt)