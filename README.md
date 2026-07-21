# Applied Analytics Mini Project

This project loads a small CSV file into a SQLite database and calculates city-level KPI values.

## Folder structure
- data/raw: raw CSV input data
- data/db: SQLite database output
- src: ETL and KPI scripts
- tests: pytest tests

## Run commands
```bash
pip install -r requirements.txt
python src/etl_load_sqlite.py
python src/kpi_city.py
pytest -q
```
