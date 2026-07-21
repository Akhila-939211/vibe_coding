import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "db" / "analytics.db"


def city_kpi(city: str) -> list[dict[str, object]]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT city, COUNT(*) AS customer_count, AVG(monthly_spend) AS avg_spend, AVG(churned) AS churn_rate FROM customers_raw WHERE city = ? GROUP BY city",
        (city,),
    )
    rows = cursor.fetchall()
    conn.close()

    result = []
    for row in rows:
        result.append(
            {
                "city": row[0],
                "customer_count": row[1],
                "avg_spend": row[2],
                "churn_rate": row[3],
            }
        )
    return result


if __name__ == "__main__":
    print(city_kpi("Mumbai"))
    print(city_kpi("Mumbai' OR 1=1 --"))
