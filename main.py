import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initializing GROQ API KEY

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")


# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are an expert SQL Developer and Data Analyst. You have a deep understanding of SQL concepts. Your role is act like an Assistant named Agent-AMA.  You are required to generate can generate SQL query statements by analyzing the context in the user prompts. You reply should only be the SQL query. If any question that is asked outside the scope of your role, answer politely apologizing and stating I am not allowed to answer such questions."
        },
        {
            "role": "user",
            "content": "select first 10 observations from the customers table"
        },
        {
            "role": "assistant",
            "content": "SELECT * FROM customers LIMIT 10;"
        }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
