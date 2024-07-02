from langchain.memory import ConversationEntityMemory

def create_memory(llm):
    return ConversationEntityMemory(llm=llm)
