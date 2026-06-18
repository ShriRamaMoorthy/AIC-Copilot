from langgraph.graph import(StateGraph,END)
from state.career_state import(CareerState)
from agents.graph_resume_agent import(resume_agent)
from agents.graph_job_agent import(job_agent)
from agents.graph_match_agent import(match_agent)

graph = StateGraph(CareerState)

graph.add_node("graph_resume_agent",resume_agent)
graph.add_node("graph_job_agent",job_agent)
graph.add_node("graph_match_agent",match_agent)
graph.set_entry_point("graph_resume_agent")
graph.add_edge("graph_resume_agent","graph_job_agent")
graph.add_edge("graph_job_agent","graph_match_agent")
graph.add_edge("graph_match_agent",END)

career_graph = graph.compile()
