from utils.matching import(calculate_match_score)

def match_agent(state):
    state["match_result"] = (calculate_match_score(
        state['resume_data'].get("skills",[]),
        state["job_skills"]
    ))
    return state