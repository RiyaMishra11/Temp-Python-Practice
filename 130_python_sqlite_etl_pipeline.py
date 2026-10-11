"""
130 - SQLite ETL Pipeline
Learn: Extract, Transform, Load (ETL), parameterized SQL, and transactions.
Uses only the Python standard library.

Run:
    python 130_python_sqlite_etl_pipeline.py
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("etl_demo.db")


def extract() -> list[tuple[str, str, int, float]]:
    """Demo source data; replace this function with CSV/API extraction."""
    return [
        (" O-1001 ", "riya", 2, 50.0),
        ("O-1002", "AMAN ", 1, 250.0),
        ("O-1003", "Neha", 3, 20.0),
        ("O-1002", "AMAN ", 1, 250.0),  # duplicate source record
        ("O-1004", "Kabir", 0, 100.0),  # invalid quantity
    ]


def transform(rows: list[tuple[str, str, int, float]]) -> list[tuple[str, str, int, float, float]]:
    cleaned = []
    seen = set()

    for order_id, customer, quantity, unit_price in rows:
        order_id = order_id.strip().upper()
        customer = customer.strip().title()
        key = (order_id, customer, quantity, unit_price)

        if key in seen:
            continue
        seen.add(key)

        if not order_id or not customer or quantity <= 0 or unit_price < 0:
            continue

        cleaned.append((order_id, customer, quantity, unit_price, quantity * unit_price))
    return cleaned


def load(rows: list[tuple[str, str, int, float, float]]) -> None:
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                customer TEXT NOT NULL,
                quantity INTEGER NOT NULL CHECK(quantity > 0),
                unit_price REAL NOT NULL CHECK(unit_price >= 0),
                revenue REAL NOT NULL CHECK(revenue >= 0)
            )
        """)
        connection.executemany("""
            INSERT INTO orders (order_id, customer, quantity, unit_price, revenue)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(order_id) DO UPDATE SET
                customer=excluded.customer,
                quantity=excluded.quantity,
                unit_price=excluded.unit_price,
                revenue=excluded.revenue
        """, rows)


def report() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        print("\\nORDERS")
        for row in connection.execute(
            "SELECT order_id, customer, quantity, unit_price, revenue "
            "FROM orders ORDER BY order_id"
        ):
            print(row)
        total = connection.execute("SELECT COALESCE(SUM(revenue), 0) FROM orders").fetchone()[0]
        print(f"\\nTotal revenue: {total:.2f}")


def main() -> None:
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)
    print(f"Extracted {len(extracted)} records; loaded {len(transformed)} valid unique records.")
    report()
    print(f"Database file: {DB_PATH.resolve()}")


if __name__ == "__main__":
    main()
