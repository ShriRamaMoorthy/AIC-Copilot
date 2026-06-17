from agents.resume_optimizer import (optimize_resume)

resume_text = """
Built Machine Learning models using Python.
Worked with SQL databases.
"""

job_description = """
Machine Learning Engineer

Required:
Python 
Tensorflow
Docker
AWS
"""

missing_skills=["Docker","AWS"]

result = optimize_resume(resume_text, job_description,missing_skills)

print(result)