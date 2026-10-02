"""94 - SQLite Database Manager"""
import sqlite3

class DatabaseManager:
    def __init__(self, database="app.db"):
        self.database = database

    def create_table(self):
        with sqlite3.connect(self.database) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            """)

    def add_user(self, name, email):
        with sqlite3.connect(self.database) as conn:
            conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )

    def get_users(self):
        with sqlite3.connect(self.database) as conn:
            return conn.execute(
                "SELECT id, name, email FROM users"
            ).fetchall()

    def delete_user(self, user_id):
        with sqlite3.connect(self.database) as conn:
            return conn.execute(
                "DELETE FROM users WHERE id = ?", (user_id,)
            ).rowcount > 0

def main():
    db = DatabaseManager("demo_users.db")
    db.create_table()
    print("Database ready.")
    print("Users:", db.get_users())

if __name__ == "__main__":
    main()
