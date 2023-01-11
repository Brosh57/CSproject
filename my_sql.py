import mysql.connector
import os

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "roshan2004",
    database = "email_data"
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS data")
cur.execute("CREATE TABLE data (email TEXT, count INTEGER)")

fname = open("mbox.txt")

for fn in fname:
    if fn.startswith("From:") :
        values = fn.split()
        value = values[1]
        cur.execute('SELECT email FROM data WHERE email = %s',(value,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO data (email,count) VALUES (%s,1)',(value,))
        else:
            cur.execute('UPDATE data SET count = count + 1 WHERE email = %s',(value,))
        conn.commit()

cur.close()

