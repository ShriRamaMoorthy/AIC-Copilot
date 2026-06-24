import json
import re
from utils.llm import ask_llm
from prompts.resume_parser_prompt import (RESUME_PARSER_PROMPT)
import copy

EMPTY_RESUME = {
        "name":"",
        "email":"",
        "phone":"",
        "linkedin":"",
        "github":"",
        "summary":"",
        "skills":[],
        "education":[],
        "experience":[],
        "projects":[],
        "certifications":[],
        "achievements":[]
    }


def parse_resume(resume_text):

    prompt = RESUME_PARSER_PROMPT.replace(
    "RESUME_CONTENT",
    resume_text
)

    response = ask_llm(prompt)

    response = re.sub(
        r"```json|```",
        "",
        response
    ).strip()
    try:
        parsed_data = json.loads(response)
        for key in EMPTY_RESUME:
            parsed_data.setdefault(key,copy.deepcopy(EMPTY_RESUME[key]))
        return parsed_data
        #return json.loads(response)

    except Exception as e:
        error_resume = copy.deepcopy(EMPTY_RESUME)
        error_resume["error"] = str(e)
        error_resume["raw_response"] =  response
        return error_resume