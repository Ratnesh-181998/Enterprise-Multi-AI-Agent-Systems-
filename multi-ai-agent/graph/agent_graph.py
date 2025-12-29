from langgraph.graph import StateGraph
from agents.search_agent import search_agent
from agents.reasoning_agent import reasoning_agent
from agents.answer_agent import answer_agent

class AgentState(dict):
    pass

builder = StateGraph(AgentState)
builder.add_node("search", search_agent)
builder.add_node("reason", reasoning_agent)
builder.add_node("answer", answer_agent)
builder.set_entry_point("search")
builder.add_edge("search", "reason")
builder.add_edge("reason", "answer")
graph = builder.compile()
