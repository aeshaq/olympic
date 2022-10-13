import sqlite3
conn = sqlite3.connect("lumber.db")
cur = conn.cursor()

sql = """
    CREATE TABLE LUMBER (
        date TEXT,
        open INTEGER,
        high INTEGER,
        low INTEGER,
        close INTEGER,
        adj_close INTEGER,
        volume INTEGER
    ) """


cur.execute(sql)
print("Lumber.db has been created \n")

with open('LumberFut_clean.csv', 'r') as file:
    for row in file:
        cur.execute("INSERT INTO LUMBER VALUES (?,?,?,?,?,?,?)", row.split(","))
        conn.commit()


print("Values added to lumber! \n")

conn.commit()
conn.close()