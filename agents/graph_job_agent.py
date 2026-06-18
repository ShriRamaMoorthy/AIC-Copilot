from agents.job_parser import extract_job_skills

def job_agent(state):
    result = extract_job_skills(state["job_description"])
    state['job_skills']=result.get("skills",[])
    return state