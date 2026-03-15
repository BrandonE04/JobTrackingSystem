import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

try:
    cur.execute('''CREATE TABLE JOB(
    Title TEXT NOT NULL,
    Company TEXT NOT NULL,
    Status TEXT NOT NULL,
    ID INTEGER PRIMARY KEY NOT NULL);
    ''')
    print('database created')
except:
    print('database already exists')

conn.close()