from llm_agent import generate_sql_query, generate_human_readable_response
import database

def main():
    print("Welcome to Agent AMA!")
    while True:
        user_input = input("Ask your question (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        # Generate SQL query from user input
        sql_query = generate_sql_query(user_input)

        # Execute SQL query and fetch results
        results = database.execute_query(sql_query)

        # Generate human-readable response from SQL query results
        human_readable_response = generate_human_readable_response(results)
        
        print(f"Answer: {human_readable_response}")

if __name__ == "__main__":
    main()