from fastapi import FastAPI
from graph.agent_graph import graph

app = FastAPI()

@app.post("/query")
def run_agent(query: str):
    result = graph.invoke({"query": query})
    return {"answer": result["final_answer"]}
