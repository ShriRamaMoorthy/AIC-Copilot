from langgraph.graph import(StateGraph,END)
from state.career_state import(CareerState)
from agents.graph_resume_agent import(resume_agent)
from agents.graph_job_agent import(job_agent)
from agents.graph_match_agent import(match_agent)
from agents.graph_recommendation_agent import(graph_recommendation_agent)
from agents.graph_optimizer_agent import(graph_optimizer_agent)
from agents.graph_cover_letter_agent import(graph_cover_letter_agent)
from agents.graph_rag_resume_optimizer_agent import(graph_rag_resume_optimizer_agent)

def route_after_match(state):
    score = state["match_result"]["match_score"]
    print(f"\nRouting Decision => Match Score: {score}")
    if score>=80:
        return "cover_letter"
    return "recommendation"

graph = StateGraph(CareerState)

graph.add_node("graph_resume_agent",resume_agent)
graph.add_node("graph_job_agent",job_agent)
graph.add_node("graph_match_agent",match_agent)
graph.add_node("graph_recommendation_agent",graph_recommendation_agent)
graph.add_node("graph_rag_resume_optimizer_agent",graph_rag_resume_optimizer_agent)
graph.add_node("graph_cover_letter_agent",graph_cover_letter_agent)
graph.set_entry_point("graph_resume_agent")


graph.add_edge("graph_resume_agent","graph_job_agent")
graph.add_edge("graph_job_agent","graph_match_agent")
#graph.add_edge("graph_match_agent","graph_recommendation_agent")
graph.add_conditional_edges(
    "graph_match_agent",
    route_after_match,
    {
        "cover_letter":"graph_cover_letter_agent",
        "recommendation":"graph_recommendation_agent"
    }
    )
graph.add_edge("graph_recommendation_agent","graph_rag_resume_optimizer_agent")
graph.add_edge("graph_rag_resume_optimizer_agent","graph_cover_letter_agent")
graph.add_edge("graph_cover_letter_agent",END)

career_graph = graph.compile()
