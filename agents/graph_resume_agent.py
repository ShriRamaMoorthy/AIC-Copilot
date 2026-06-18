from agents.resume_parser import parse_resume

def resume_agent(state):
    state['resume_data'] = parse_resume(state['resume_text'])
    return state