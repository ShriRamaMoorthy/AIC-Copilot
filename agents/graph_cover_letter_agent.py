from agents.cover_letter_generator import(generate_cover_letter)

def graph_cover_letter_agent(state):
    print("\nExecuting graph_cover_letter_agent")
    state['cover_letter'] = (
        generate_cover_letter(
            state["resume_data"],
            state["job_description"]
        )
    )
    return state