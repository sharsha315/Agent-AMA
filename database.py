import sqlite3

def execute_query(query):
    try:
        conn = sqlite3.connect('northwind.db')
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except sqlite3.Error as e:
        return f"An error occurred: {e}"
