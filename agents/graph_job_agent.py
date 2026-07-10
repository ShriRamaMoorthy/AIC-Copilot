from agents.job_parser import extract_job_skills

def job_agent(state):
    print("\nExecuting graph_job_agent")
    job_data = extract_job_skills(state["job_description"])
    #state['job_skills']=result.get("skills",[])
    state['job_data']=job_data
    state['job_skills']=job_data.get("skills",[])
    return state