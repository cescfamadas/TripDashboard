import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('tripdb.db', check_same_thread=False)

    def query(self, query, params=None):
        cursor = self.conn.cursor()
        cursor.execute(query, params or [])
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        return rows, columns

    def __del__(self):
        self.conn.close()
