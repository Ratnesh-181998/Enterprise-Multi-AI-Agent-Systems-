import streamlit as st
import requests

st.title("Multi-AI Agent")

query = st.text_input("Ask something")

if st.button("Run"):
    r = requests.post("http://localhost:8000/query", params={"query": query})
    st.write(r.json()["answer"])
