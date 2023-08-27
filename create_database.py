import sqlite3

# Connect to the database (will create a new file named "employees.db")
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Create the Employee table
cursor.execute('''
CREATE TABLE Employee (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    start_time DATETIME,
    end_time DATETIME
)
''')

# Insert sample employees
cursor.executemany('''
INSERT INTO Employee (name) VALUES (?)
''', [('John Doe',), ('Jane Smith',), ('Alice Johnson',)])

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database, table, and sample data created successfully!")
