import os
from langchain_community.utilities import SQLDatabase

def initialize_database(db_path):
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"The Database file {db_path} does not exist.")
    
    return SQLDatabase.from_uri(f"sqlite:///{db_path}")
