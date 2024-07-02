import os
from langchain_groq import ChatGroq

def create_llm():
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    return ChatGroq(
        temperature=0,
        model="llama3-70b-8192",
        api_key=GROQ_API_KEY
    )
