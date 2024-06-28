# Agent AMA - An SQL Querying AI Agent

Agent-AMA is an AI-powered agent designed to interact with SQL databases, perform reasoning before taking action, and generate SQL queries based on user inputs. This agent uses the ReAct prompting technique and Langchain's ConversationEntityMemory feature to enhance contextual understanding and improve user interactions. It leverages the power of the Llama-3 LLM (provided by GROQ) to generate natural language responses and SQL queries.

## Features

- Interactive SQL Querying: Engage with the SQL database through natural language questions.
- ReAct Prompting: Utilizes a reasoning step before acting to ensure accurate query generation.
- Memory Feature: Remembers previous interactions for a more contextually aware conversation.
- SQLite Database: Interacts with an SQLite database for executing queries.
- Error Handling: Includes robust error handling to manage and retry failed queries.

## Prerequisites

- Python 3.10 or higher
- SQLite database file (northwind.db)
- GROQ API key

## Setup

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/Agent-AMA.git
cd Agent-AMA

```

2. Create a Virtual Environment:

- **Create a virtual environment:**
   ```bash
   python -m venv env
   ```

- **Activate the virtual environment:**
    - On Windows:
    ```bash
    .\env\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source env/bin/activate
    ```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

4. Setup Environmental Variables:
Create a .env file in the project root and add your GROQ API key:

```bash
GROQ_API_KEY=your_groq_api_key
```

5. Ensure the Database file exists:
Make sure the `northwind.db` file is present in the project directory.

## Usage

Run the `main.py` script to start the interactive command-line interface:
```bash
python main.py
```

## Contribution Guide
We welcome contributions to improve Agent-AMA. Please follow standard coding practices and ensure your code is well-documented. Feel free to open a pull request with your changes, and we will review it as soon as possible. Thank you for your contributions!

## Support

If you like this project, please give it a star on GitHub!

Follow me on social media for more updates:

- [Tublian](https://www.tublian.com/profile/sharsha315)
- [GitHub](https://github.com/sharsha315)
- [X](https://www.X.com/sharsha315)
- [LinkedIn](https://linkedin.com/in/sharsha315)

Thank you for your support!