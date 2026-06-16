import json
import re

from utils.llm import ask_llm

def match_resume_to_job(resume_data,job_description):
    prompt = f"""
You are an expert recruiter.
Compare the candidate profile with the job description.
Return ONLY JSON.
Do not create additional keys.
Do not rename keys.

{{
"match_score": integer from 0 to 100,
"matched_skills":[],
"missing_skills":[],
"recommendations":[]
}}

Candidate:
{resume_data}

Job Description:
{job_description}

"""
    response = ask_llm(prompt)
    response = response.strip()
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        result =  json.loads(response)
        result.setdefault("match_score", 0)
        result.setdefault("matched_skills", [])
        result.setdefault("missing_skills", [])
        result.setdefault("recommendations", [])
        return result
    
    except Exception as e:
        return {
            "error":str(e),
            "raw_response":response
        }   