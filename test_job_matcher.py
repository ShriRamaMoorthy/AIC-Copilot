from agents.job_matcher import (
    match_resume_to_job
)

resume_data = {
    "skills": [
        "Python",
        "SQL",
        "TensorFlow"
    ]
}

job_description = """
Machine Learning Engineer

Required Skills:

Python
SQL
Docker
Kubernetes
TensorFlow
AWS
"""

result = match_resume_to_job(
    resume_data,
    job_description
)

print(result)