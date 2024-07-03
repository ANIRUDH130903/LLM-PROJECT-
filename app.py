import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
st.title("LLM MODEL")
repo_id="mistralai/Mistral-7B-Instruct-v0.2"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=120,temperature=0.7)
ip = st.text_input("Enter your question")
btn = st.button("Ask")
if btn:
  st.write(llm.invoke(ip))
