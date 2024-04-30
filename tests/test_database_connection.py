import pytest
from library.database_connection import DatabaseConnection

# A pytest object to past to each test using the Database connection
@pytest.fixture
def db_connection():
    conn = DatabaseConnection("test.db")
    yield conn



"""
When I seed the database
I can access thoes records
"""

def test_database_connection(db_connection):

    # Delete any previous test tables then create new one for current test
    db_connection.execute("DROP TABLE IF EXISTS test_table;")
    db_connection.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255))")

    # Insert new record then fetch all records to see if record stored correctly
    db_connection.execute("INSERT INTO test_table (name) VALUES (?)", ["first_record"])
    row = db_connection.execute("SELECT * FROM test_table")

    result = dict(row)

    assert result == { 1: "first_record" }

