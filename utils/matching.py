def calculate_match_score(resume_skills,job_skills):
    resume_skills={
        skill.lower()
        for skill in resume_skills
    }

    job_skills={
        skill.lower()
        for skill in job_skills
    }

    matched = list(
        resume_skills.intersection(
            job_skills
        )
    )

    missing = list(
        job_skills.difference(
            resume_skills
        )
    )

    if len(job_skills) == 0:
        score=0
    else:
        score = round(
            len(matched) / len(job_skills)*100
        )
    return {
        "match_score":score,
        "matched_skills":matched,
        "missing_skills":missing
    }