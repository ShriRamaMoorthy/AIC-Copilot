import json
import re

from utils.llm import ask_llm

def match_resume_to_job(resume_data,job_description):
    prompt = f"""
You are an expert recruiter.
Compare the candidate profile with the job description.
Return ONLY JSON.

{{
"match_score":0,
"matched_skills":[],
"missing_skills":[],
"recommendation":[]
}}

Candidate:
{resume_data}

Job Description:
{job_description}

"""
    response = ask_llm(prompt)
    response = re.sub(
        r"```json```",
        "",
        response
    ).strip()

    try:
        return json.loads(response)
    except Exception as e:
        return {
            "error":str(e),
            "raw_response":response
        }