from langchain_groq import ChatGroq

llm = ChatGroq(model="llama3-70b-8192")

def answer_agent(state):
    response = llm.invoke(f"Answer clearly: {state['analysis']}")
    return {"final_answer": response.content}
