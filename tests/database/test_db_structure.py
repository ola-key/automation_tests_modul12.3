import pytest
import sqlite3
from modules.common.database import Database



@pytest.mark.database
def test_db_structure():
    db_path = "db/become_qa_auto.db"
    db = sqlite3.connect(db_path)
    cursor = db.cursor()
    tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        columns = cursor.execute(f"PRAGMA table_info({table_name});").fetchall()
        for col in columns:
            print(f"  Column: {col[1]} | Type: {col[2]}")
    db.close()
    