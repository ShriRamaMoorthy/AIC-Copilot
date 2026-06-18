from agents.resume_optimizer import (optimize_resume)

def graph_optimizer_agent(state):
    state['optimized_resume']=(
        optimize_resume(
            state["resume_text"],
            state["job_description"],
            state["match_result"]["missing_skills"]
        )
    )
    return state