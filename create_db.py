import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS table_name (id INTEGER PRIMARY KEY, column1 TEXT, column2 TEXT)')
conn.commit()
conn.close()
