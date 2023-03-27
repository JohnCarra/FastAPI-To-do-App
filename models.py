from pydantic import BaseModel
import psycopg2
import os


class ToDoItem(BaseModel):
    name: str
    description: str
    due_date: str


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    def execute_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        cursor.close()

    def fetch_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        return result

    def fetch_single_query(self, query, values=None):
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        return result
