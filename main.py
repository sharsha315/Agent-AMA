import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.prompt import SQL_FUNCTIONS_SUFFIX
from langchain.memory import ConversationEntityMemory
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    MessagesPlaceholder
)

# Load environmental variables from .env file
load_dotenv()

# Initialize GROQ API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initializing ChatGroq, with llama-3 LLM
llm = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=GROQ_API_KEY
)

# Initializing the Database
db_path = "/workspaces/Agent-AMA/northwind.db"

if not os.path.exists(db_path):
    raise FileNotFoundError(f"The Database file {db_path} does not exist.")

db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

# Create a Custom SQL Agent - AgentAMA

# 1. Create tools
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
context = toolkit.get_context()
tools = toolkit.get_tools()

# 2. Create ReAct prompt
system_prompt = """
You are an agent named "Agent-AMA", designed to interact with the SQL database.
You are an agent that does a reasoning step before the acting.
Given an input question, create a syntactically correct dialect query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
If the question does not seem related to the database, just return "I am Sorry, I only answer questions related to the database" as the answer.
If you come across the Final Answer immediately stop Thought, Action Process and return the answer framing a very good sentence.

Answer the following questions as best you can. You have access to the following tools:
{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Final Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

messages = [
    SystemMessagePromptTemplate.from_template(system_prompt),
    HumanMessagePromptTemplate.from_template("{input}"),
    AIMessagePromptTemplate.from_template(SQL_FUNCTIONS_SUFFIX),
    ("human", "{agent_scratchpad}"),
]

prompt = ChatPromptTemplate.from_messages(messages)
prompt = prompt.partial(**context)

# Create Memory
memory = ConversationEntityMemory(llm=llm)

# 3. Create Agent
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# Run agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# Main function
def main():
    print("\nWelcome!!!")
    print("\nI am Agent-AMA,")
    
    while True:
        user_input = input("\nEnter your query (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("\nGoodbye!!!\n")
            break
        try:
            memory.load_memory_variables({"input": "Can you list the tables available in the database?"})
            result = agent_executor.invoke({"input": user_input})
            memory.save_context({"input": result["input"]}, {"output": result["output"]})
            
            print()
            print("****"*10)
            print(f"\nYou: {result['input']}\nAgent-AMA: {result['output']}")
            print()
            print("****"*10)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
