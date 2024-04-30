import sqlite3

class DatabaseConnection:
    # init with databasename, can be change for tests
    def __init__(self, db_name):
        self.db_name = db_name


    # Function connects to SQLite, only to be used within class
    def _connect(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        connection.cursor()
        return connection


    # Function to allow seed data from SQL file to be used, useful for testing
    def seed(self, file):
        try:
            with self._connect() as conn, open(file, "r") as f:
                sql_seed = f.read()
                conn.executescript(sql_seed)
                conn.commit()
        except sqlite3.Error as error:
            print(f"Error seeding database with {file}: {error}")


    # Function to process queries to SQLite database
    def execute(self, query, params=None):
        try:
            with self._connect() as conn:
                cursor = conn.execute(query, params or ())
                if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                    conn.commit()
                if cursor.description:
                    result = cursor.fetchall()
                else:
                    result = None
                return result
        except sqlite3.Error as error:
            print("Error while executing query:", error)
            return None



