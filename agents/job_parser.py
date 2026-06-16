import json
import re

from utils.llm import ask_llm

def extract_job_skills(job_description):
    prompt = f"""
Extract al required skills from this description.
Return ONLY JSON.

{{
"skills":[]
}}

Job Description:
{job_description}
"""
    response = ask_llm(prompt)
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        return json.loads(response)
    except Exception as e:
        return{
            "error":str(e),
            "raw_response":response
        }