from agents.job_parser import extract_job_skills
from utils.matching import calculate_match_score


resume_skills = [
    "Python",
    "SQL",
    "TensorFlow"
]

job_description = """
Machine Learning Engineer
Required Skills:
Python
SQL
Docker
AWS
TensorFlow
"""

job_data = extract_job_skills(
    job_description
)

result = calculate_match_score(
    resume_skills,
    job_data["skills"]
)

print(result)