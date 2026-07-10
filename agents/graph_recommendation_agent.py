from agents.recommendation_agent import(generate_recommendation)

def graph_recommendation_agent(state):
    print("\nExecuting graph_recommendation_agent")
    state["recommendations"]=(
        generate_recommendation(
            state['match_result']["missing_skills"], state['job_description']
        )
    )
    return state