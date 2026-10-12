"""134 - SQLite Sales Analytics | Uses Python standard library only"""
import sqlite3

def main():
    with sqlite3.connect(":memory:") as connection:
        connection.execute("""
            CREATE TABLE sales (
                sale_id INTEGER PRIMARY KEY,
                region TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount >= 0)
            )
        """)
        connection.executemany(
            "INSERT INTO sales(region, category, amount) VALUES (?, ?, ?)",
            [
                ("North", "Office", 1200), ("South", "Tech", 3500),
                ("North", "Tech", 2400), ("West", "Office", 900),
                ("South", "Office", 1500), ("West", "Tech", 2800),
                ("North", "Office", 700), ("South", "Tech", 1800),
            ],
        )

        print("SALES BY REGION")
        for row in connection.execute("""
            SELECT region, SUM(amount) AS total_sales, COUNT(*) AS transactions
            FROM sales GROUP BY region ORDER BY total_sales DESC
        """):
            print(row)

        print("\\nCATEGORIES WITH SALES ABOVE 3000")
        for row in connection.execute("""
            SELECT category, SUM(amount) AS total_sales FROM sales
            GROUP BY category HAVING SUM(amount) > ? ORDER BY total_sales DESC
        """, (3000,)):
            print(row)

        count, revenue, average = connection.execute("""
            SELECT COUNT(*), ROUND(SUM(amount), 2), ROUND(AVG(amount), 2) FROM sales
        """).fetchone()
        print(f"\\nTransactions: {count} | Revenue: {revenue} | Average sale: {average}")

if __name__ == "__main__":
    main()
