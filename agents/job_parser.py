import json
import re

from utils.llm import ask_llm

def extract_job_skills(job_description):
    prompt = f"""
You are an expert Job Description Parser.
Extract structured information from the job description.

IMPORTANT RULES
1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. Do NOT explain anything.
4. Do NOT invent information.
5. If information is missing:
    - use "" for strings
    - use [] for arrays

Return EXACTLY this schema:
{{
"job_title":"",
"skills":[],
"required_skills":[],
"preferred_skills":[],
"required_experience":"",
"preferred_experience":"",
"required_education":"",
"preferred_education":"",
"certifications":[],
"responsibilities":[],
"soft_skills":[],
"keywords":[]
}}

Job Description:
{job_description}
"""
    
    EMPTY_JOB = {
        "job_title":"",
        "skills":[],
        "required_skills":[],
        "required_experience": "",
        "preferred_experience": "",
        "required_education": "",
        "preferred_education": "",
        "certifications": [],
        "responsibilities": [],
        "soft_skills": [],
        "keywords": []
    }

    response = ask_llm(prompt)
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()

    try:
        parsed = json.loads(response)

        for key in EMPTY_JOB:
            parsed.setdefault(key,EMPTY_JOB[key])
        
        return parsed
    
    except Exception as e:
        error_job = EMPTY_JOB.copy()
        error_job["error"]=str(e)
        error_job["raw_response"]=response
        return error_job