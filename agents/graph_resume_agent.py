from agents.resume_parser import parse_resume

def resume_agent(state):
    print("\nExecuting graph_resume_agent")
    state['resume_data'] = parse_resume(state['resume_text'])
    return state