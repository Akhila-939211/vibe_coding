import sqlite3
from pathlib import Path

from src.etl_load_sqlite import load_csv_to_sqlite
from src.kpi_city import city_kpi

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "data" / "db" / "analytics.db"


def test_city_kpi_happy_path():
    load_csv_to_sqlite()
    result = city_kpi("Mumbai")

    assert len(result) == 1
    assert result[0]["city"] == "Mumbai"
    assert result[0]["customer_count"] == 3


def test_city_kpi_injection_attempt():
    load_csv_to_sqlite()
    result = city_kpi("Mumbai' OR 1=1 --")

    assert result == []
