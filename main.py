import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor
from langchain.memory import ConversationEntityMemory
from llm import create_llm
from memory import create_memory
from database import initialize_database
from agent import create_custom_agent

# Load environmental variables from .env file
load_dotenv()

# Initialize LLM and Memory
llm = create_llm()
memory = create_memory(llm)

# Initialize Database
db = initialize_database("/workspaces/Agent-AMA/northwind.db")

# Create Custom SQL Agent
agent_executor = create_custom_agent(llm, db)

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
