import json
import re
from utils.llm import ask_llm

from prompts.resume_parser_prompt import (
    RESUME_PARSER_PROMPT
)


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
        return json.loads(response)

    except Exception as e:

        return {
            "error":str(e),
            "raw_response": response
        }