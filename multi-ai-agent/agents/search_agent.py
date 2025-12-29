from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_agent(state):
    query = state["query"]
    result = tavily.search(query=query, max_results=3)
    return {"search_results": result}
