from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"]="langchain_groq_chatbot"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, Please respond to the user queries."),
        ("user", "Question:{question}")
    ]
)


st.title('Langchain Chatbot With Groq API')
input_text = st.text_input("Search the topic you want")

llm = ChatGroq()
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

