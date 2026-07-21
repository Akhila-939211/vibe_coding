import csv
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT / "data" / "raw" / "customers_raw.csv"
DB_PATH = ROOT / "data" / "db" / "analytics.db"


def load_csv_to_sqlite(csv_path: Path = CSV_PATH, db_path: Path = DB_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS customers_raw")
    cursor.execute(
        """
        CREATE TABLE customers_raw (
            customer_id INTEGER,
            city TEXT,
            monthly_spend REAL,
            churned INTEGER
        )
        """
    )

    with csv_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            cursor.execute(
                "INSERT INTO customers_raw (customer_id, city, monthly_spend, churned) VALUES (?, ?, ?, ?)",
                (
                    int(row["customer_id"]),
                    row["city"],
                    float(row["monthly_spend"]),
                    int(row["churned"]),
                ),
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    load_csv_to_sqlite()
    print(f"Loaded data into {DB_PATH}")
