from agents.cover_letter_generator import(generate_cover_letter)

def graph_cover_letter_agent(state):
    print("\nExecuting graph_cover_letter_agent")
    resume_content = state.get(
        "optimized_resume",
        state["resume_text"]
    )
    state['cover_letter'] = (
        generate_cover_letter(
            resume_content,
            state["job_description"]
        )
    )
    return state