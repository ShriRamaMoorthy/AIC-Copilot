import re


# ---------------------------------------------------
# Experience
# ---------------------------------------------------

def extract_years(text):

    if not text:
        return 0

    matches = re.findall(r"(\d+)\+?\s*years?", str(text).lower())

    if matches:
        return max(int(x) for x in matches)

    return 0


# ---------------------------------------------------
# Skill Score
# ---------------------------------------------------

def calculate_skill_score(resume_skills, job_skills):

    if not job_skills:
        return 0

    resume = {s.lower() for s in resume_skills}
    job = {s.lower() for s in job_skills}

    matched = resume.intersection(job)

    return round(len(matched) / len(job) * 10, 1)


# ---------------------------------------------------
# Project Score
# ---------------------------------------------------

def calculate_project_score(projects, job_skills):

    if not projects:
        return 0

    project_text = " ".join(

        str(project.get("title", "")) + " " +
        str(project.get("description", "")) + " " +
        " ".join(project.get("technologies", []))

        for project in projects

    ).lower()

    matched = 0

    for skill in job_skills:

        if skill.lower() in project_text:
            matched += 1

    return round((matched / max(len(job_skills), 1)) * 10)


# ---------------------------------------------------
# Education Score
# ---------------------------------------------------

def calculate_education_score(education, job_data):

    if not education:
        return 0

    education_text = " ".join(
        item.get("degree", "")
        for item in education
    ).lower()

    jd_education = " ".join([
        job_data.get("required_education", ""),
        job_data.get("preferred_education", "")
    ]).lower()

    score = 0

    # Highest qualification

    if any(x in education_text for x in
           ["phd", "doctor", "doctorate"]):

        score = 10

    elif any(x in education_text for x in
             ["m.tech", "mtech", "m.sc", "msc", "master", "ms"]):

        score = 8

    elif any(x in education_text for x in
             ["b.tech", "btech", "b.sc", "bsc", "b.e", "be", "bachelor", "bs"]):

        score = 6

    # Domain relevance

    domains = [

        "artificial intelligence",
        "machine learning",
        "computer science",
        "data science",
        "software engineering"

    ]

    for domain in domains:

        if domain in education_text and domain in jd_education:
            score += 1

    return min(score, 10)


# ---------------------------------------------------
# Experience Score
# ---------------------------------------------------

def calculate_experience_score(experience, job_data):

    required_years = extract_years(
        job_data.get("required_experience", "")
    )

    if not experience:
        return 0

    experience_text = " ".join(
        str(x)
        for x in experience
    )

    candidate_years = extract_years(experience_text)

    if candidate_years == 0:

        return 5

    if required_years == 0:

        return min(candidate_years, 10)

    score = (candidate_years / required_years) * 10

    return round(min(score, 10), 1)


# ---------------------------------------------------
# Certification Score
# ---------------------------------------------------

def calculate_certification_score(certifications):

    if not certifications:
        return 0

    return min(len(certifications) * 2, 10)


# ---------------------------------------------------
# Final ATS Score
# ---------------------------------------------------

def calculate_ats_score(resume_data, job_data):

    job_skills = job_data.get(
        "required_skills",
        job_data.get("skills", [])
    )

    skill_score = calculate_skill_score(
        resume_data.get("skills", []),
        job_skills
    )

    project_score = calculate_project_score(
        resume_data.get("projects", []),
        job_skills
    )

    education_score = calculate_education_score(
        resume_data.get("education", []),
        job_data
    )

    experience_score = calculate_experience_score(
        resume_data.get("experience", []),
        job_data
    )

    certification_score = calculate_certification_score(
        resume_data.get("certifications", [])
    )

    overall_score = round(

        (
            skill_score * 0.40 +
            experience_score * 0.25 +
            project_score * 0.15 +
            education_score * 0.10 +
            certification_score * 0.10

        ) * 10,

        1

    )

    return {

        "skill_score": skill_score,
        "project_score": project_score,
        "education_score": education_score,
        "experience_score": experience_score,
        "certification_score": certification_score,
        "overall_ats_score": overall_score

    }