import os
import asyncpg
from pydantic import BaseModel

# Define the To-Do Item model


class ToDoItem(BaseModel):
    name: str
    description: str
    due_date: str

# Define the Database class


class Database:
    async def connect(self):
        self.conn = await asyncpg.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            database=os.getenv("DB_NAME", "default_db_name"),
            user=os.getenv("DB_USER", "default_db_user"),
            password=os.getenv("DB_PASSWORD", "default_db_password"),
            port=os.getenv("DB_PORT", 5432)
        )
        return self.conn

    async def disconnect(self):
        await self.conn.close()

    async def execute_query(self, query: str, values: tuple):
        async with self.conn.transaction():
            result = await self.conn.execute(query, *values)
        return result

    async def fetch_query(self, query: str, values: tuple = None):
        if values:
            result = await self.conn.fetch(query, *values)
        else:
            result = await self.conn.fetch(query)
        return result

    async def fetch_single_query(self, query: str, values: tuple):
        result = await self.conn.fetchrow(query, *values)
        return result
