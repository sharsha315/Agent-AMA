import sqlite3

def execute_query(query):
    conn = sqlite3.connect('northwind.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results