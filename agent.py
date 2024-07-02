from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.prompt import SQL_FUNCTIONS_SUFFIX
from langchain_core.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
from prompt import system_prompt

def create_custom_agent(llm, db):
    # Create tools
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    context = toolkit.get_context()
    tools = toolkit.get_tools()

    # Create ReAct prompt
    
    messages = [
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template("{input}"),
        AIMessagePromptTemplate.from_template(SQL_FUNCTIONS_SUFFIX),
        ("human", "{agent_scratchpad}"),
    ]

    prompt = ChatPromptTemplate.from_messages(messages)
    prompt = prompt.partial(**context)

    # Create Agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

    # Create and return Agent Executor
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
