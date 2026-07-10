import re

def extract_years_from_jd(job_description):
    """
    Extract required years from JD.
    Example:
    '3+ years'
    '5 years experience'
    """
    matches = re.findall(
        r"(\d+)\+?\s*years?",job_description.lower()
    )

    if matches:
        return max([int(x) for x in matches])
    return 0


def calculate_skill_score(resume_skills,job_skills):
    if not job_skills:
        return 0
    matched = set(skill.lower() for skill in resume_skills).intersection(set(skill.lower() for skill in job_skills))
    return round((len(matched)/len(job_skills))*10,1)

def calculate_project_score(projects,job_skills):
    if not projects:
        return 0
    project_text = "".join([
        str(project.get('title',""))+" "+
        str(project.get("description",""))+" "+
        " ".join(project.get("technologies",[]))
        for project in projects
    ]).lower()

    matched = 0

    for skill in job_skills:
        if skill.lower() in project_text:
            matched+=1
    return round((matched/max(len(job_skills),1))*10)

def calculate_education_score(education,job_description):
    if not education:
        return 0
    jd = job_description.lower()
    education_text = " ".join([
        str(item.get("degree"," "))
        for item in education
    ]).lower()

    score=0

    if "phd" in education_text:
        score+=10
    elif "m.tech" in education_text or "mtech" in education_text or "m.sc" in education_text or "msc" in education_text:
        score+=8
    elif "b.tech" in education_text or "btech" in education_text or "b.sc" in education_text or "bsc" in education_text:
        score += 6

    ai_keywords = [ "artificial intelligence","machine learning","computer science","data science"]

    for keyword in ai_keywords:
        if keyword in education_text and keyword in jd:
            score+=1
    return min(score,10)


def calculate_experience_score(experience,job_description):
    required_years = extract_years_from_jd(job_description)
    if not experience:
        return 0
    experience_text = " ".join([
        str(item) for item in experience
    ])

    years_found = re.findall(r"(\d+)\+?\s*years?",experience_text.lower())

    if not years_found:
        return 5
    
    candidate_years = max([
        int(x) for x in years_found
    ])

    if required_years == 0:
        return min(candidate_years,10)
    
    score = (candidate_years/required_years)*10

    return round(min(score,10),1)


def calculate_certification_score(certifications):
    if not certifications:
        return 0
    return min(len(certifications)*2,10)


def calculate_ats_score(resume_data,job_skills,job_description):
    skill_score = calculate_skill_score(resume_data.get("skills",[]),job_skills)
    project_score = calculate_project_score(resume_data.get("projects",[]),job_skills)
    education_score = calculate_education_score(resume_data.get("education",[]),job_description)
    experience_score = calculate_experience_score(resume_data.get("experience",[]),job_description)
    certification_score = (calculate_certification_score(resume_data.get("certifications",[])))

    overall_score = round((skill_score*0.40+experience_score*0.25+project_score*0.15+education_score*0.10+certification_score*0.10)*10,1)

    return {
        "skill_score":skill_score,
        "project_score":project_score,
        "education_score":education_score,
        "experience_score":experience_score,
        "certification_score":certification_score,
        "overall_ats_score":overall_score
    }