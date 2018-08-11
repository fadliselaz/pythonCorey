import sqlite3

conn = sqlite3.connect(":memory:")

c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#         first text,
#         last text,
#         pay integer
# )""")

# c.execute("INSERT INTO employees VALUES('fadliselaz', 'graphic', 5000)")


c.execute("SELECT * FROM employees")
#
# print(c.fetchall())
#
#
conn.commit()

conn.close()
