import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('northwind.db')
cursor = conn.cursor()

# Verify the tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:", tables)

conn.close()
