from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Test Strategy Document Generator",layout="centered")
st.title("Test Strategy Document Generator")

with st.form("Input form"):
    query=st.text_area("Give some context about application",placeholder="Example: Webbased application connected to DB2 database and backend is Mainframe")
    submitted = st.form_submit_button("Submit")

if submitted:
    with st.spinner("Agent generating test strategy document.Please wait.."):
        prompt_txt = "{query}"
        prompt_template = ChatPromptTemplate.from_template(prompt_txt)
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=os.getenv("gemini_api_key"))
        llmchain = (prompt_template | llm)
        response=llmchain.invoke({'query':query})
        st.markdown(response.content)


