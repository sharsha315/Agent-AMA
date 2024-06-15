import os
import sqlite3
import database
from groq import Groq
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


# Load environment variables from .env file
load_dotenv()

# Initializing GROQ API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY
)

system = """You are an skillfull and helpful SQL AI Agent"""

human = """{text}"""

prompt = ChatPromptTemplate.from_messages([("system", system),("human", human)]) 

chain = prompt | chat 
response = chain.invoke({"text": "Give me the SQL query to find number of items in orders table"})
print(response.content)