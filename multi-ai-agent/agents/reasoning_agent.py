from langchain_groq import ChatGroq

llm = ChatGroq(model="llama3-70b-8192")

def reasoning_agent(state):
    context = state["search_results"]
    response = llm.invoke(f"Reason based on: {context}")
    return {"analysis": response.content}
