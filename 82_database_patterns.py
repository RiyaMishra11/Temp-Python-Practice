# 82 Database Patterns
import sqlite3
c=sqlite3.connect(":memory:"); q=c.cursor()
# 1 Create table
q.execute("CREATE TABLE users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"); print("1 table created")
# 2 Insert
q.execute("INSERT INTO users(name,age) VALUES(?,?)",("Aman",22)); c.commit(); print("2",q.lastrowid)
# 3 Many inserts
q.executemany("INSERT INTO users(name,age) VALUES(?,?)",[("Riya",21),("Rahul",24),("Neha",23)]); c.commit(); print("3",q.rowcount)
# 4 Select
print("4",q.execute("SELECT * FROM users").fetchall())
# 5 Filter
print("5",q.execute("SELECT name FROM users WHERE age>=?",(23,)).fetchall())
# 6 Update
q.execute("UPDATE users SET age=? WHERE name=?", (25,"Rahul")); c.commit(); print("6",q.rowcount)
# 7 Delete
q.execute("DELETE FROM users WHERE name=?",("Riya",)); c.commit(); print("7",q.rowcount)
# 8 Aggregate
print("8",q.execute("SELECT COUNT(*),AVG(age),MAX(age) FROM users").fetchone())
# 9 Group by
q.execute("CREATE TABLE orders(user_id INTEGER,amount REAL)")
q.executemany("INSERT INTO orders VALUES(?,?)",[(1,500),(1,300),(2,900)])
print("9",q.execute("SELECT user_id,SUM(amount) FROM orders GROUP BY user_id").fetchall())
# 10 Rollback
try:
 q.execute("INSERT INTO users(name,age) VALUES(?,?)",("Temp",30)); raise ValueError
except ValueError: c.rollback()
print("10 rollback done")
# 11 Context manager
with sqlite3.connect(":memory:") as db:
 db.execute("CREATE TABLE products(id INTEGER,name TEXT)")
 db.execute("INSERT INTO products VALUES(?,?)",(1,"Laptop"))
 print("11",db.execute("SELECT * FROM products").fetchall())
c.close()
