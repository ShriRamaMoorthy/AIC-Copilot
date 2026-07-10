from utils.llm import ask_llm

def generate_recommendation(missing_skills,job_description):
    prompt = f"""
You are a senior career coach.
A candidate is applying for the following role:
{job_description}

Missing Skills:
{missing_skills}

Provide:
1. Learning recommendations.
2. Project suggestions.
3. Resume improvement suggestions.

Return concise bullet points.
"""
    return ask_llm(prompt)

