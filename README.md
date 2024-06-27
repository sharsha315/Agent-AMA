# Agent AMA

Agent AMA is a command-line SQL agent designed to assist users with SQL database queries through natural language questions. Leveraging the LangChain framework and GROQ's LLM, this project provides an interactive and intelligent querying interface without the need for a graphical UI.

## Features

- Natural Language to SQL Conversion: Converts user input into SQL queries.
- Interactive Command Line Interface: Users can type questions and receive answers directly.
- GROQ Integration: Utilizes GROQ's LLM for generating SQL queries and interpreting results.
- SQLite Database: Interacts with an SQLite database for executing queries.

## Prerequisites
- Python 3.10 or higher
- SQLite database file (northwind.db)
- GROQ API key

## Installation

1. Clone the Repository:
```bash
git clone https://github.com/yourusername/Agent-AMA.git
cd Agent-AMA

```

2. Create a Virtual Environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
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