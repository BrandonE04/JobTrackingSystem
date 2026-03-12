import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

try:
    cur.execute('''CREATE TABLE JOB(
    Name TEXT NOT NULL,
    Company TEXT NOT NULL,
    Status TEXT NOT NULL,
    ID INT PRIMARY KEY);
    ''')
    print('database created')
except:
    print('database already exists')