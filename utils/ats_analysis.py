def generate_ats_analysis(resume_data,job_data,ats_scores,match_result):
    analysis={}
    strengths=[]
    weakness=[]
    improvements=[]

    for skill in match_result["matched_skills"]:
        strengths.append(
            f"{skill.title()} matches the job requirements."
        )

    for skill in match_result["missing_skills"]:
        weakness.append(
            f"{skill.title()} is required but missing."
        )
        improvements.append(
            f"Learn {skill.title()} if relevant to your career goals."
        )

    education = resume_data.get("education",[])

    if education:
        degree = education[0].get("degree","")
        strengths.append(f"Relevant education: {degree}")
    else:
        weakness.append("Education section missing.")


    if resume_data.get("experience"):
        strengths.append("Professional experience present")
    else:
        weakness.append("No professional experience listed.")

    projects = resume_data.get("projects",[])

    if projects:
        for project in projects:
            strengths.append(f"Project: {project['title']}")
    else:
        weakness.append("No projects listed.")

    if resume_data.get("certifications"):
        strengths.append("Relevant certifications present")
    else:
        weakness.append("No certification listed.")

    if resume_data.get("achievements"):
        strengths.append("Achievements strengthen the resume.")
    else:
        weakness.append("No achievements listed.")

    analysis['strengths'] = strengths
    analysis['weakness'] = weakness
    analysis['improvements'] = improvements
    analysis['ats_scores'] = ats_scores
    
    return analysis