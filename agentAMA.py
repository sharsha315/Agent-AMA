import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType

# Load environment variables from .env file
load_dotenv()

# Initializing GROQ API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize ChatGroq
llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY
)

# Initialize the database
db_path = "/workspaces/Agent-AMA/northwind.db"
if not os.path.exists(db_path):
    raise FileNotFoundError(f"The database file {db_path} does not exist.")
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

# Create SQL Agent - Agent_AMA
agent_AMA = create_sql_agent(
    llm,
    db=db, 
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# Function to process user query
def process_query(query):
    try:
        result = agent_AMA.invoke(query)
        print("\nResult: ", result["output"])
    except Exception as e:
        print("An error occured: ", e)

# Main function
def main():
    print("Welcome!!!")
    print("I am Agent-AMA")
    while True:
        user_input = input("\nAsk your question (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        process_query(user_input)

if __name__ == "__main__":
    main()
