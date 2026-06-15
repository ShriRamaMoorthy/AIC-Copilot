RESUME_PARSER_PROMPT = """
You are an expert resume parser.

Extract the information from the resume.

IMPORTANT RULES:
1.Return ONLY valid JSON.
2.Do not include markdown.
3.Do not include explanations.
4.Use ONLY these keys:

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":[],
    "experience":[],
    "projects":[]
}}

5.If information is missing, use empty string or empty list.
6.Infer technical skills from projects and experience.
7.Never create additional keys.

Resume:

RESUME_CONTENT
"""

