import os
import aiosqlite
from pydantic import BaseModel


class ToDoItem(BaseModel):
    name: str
    description: str
    due_date: str


class Database:
    async def connect(self):
        self.conn = await aiosqlite.connect('todolist.db')
        return self.conn

    async def disconnect(self):
        await self.conn.close()

    async def execute_query(self, query: str, values: tuple):
        cursor = await self.conn.cursor()
        await cursor.execute(query, values)
        await self.conn.commit()

    async def fetch_query(self, query: str, values: tuple = None):
        cursor = await self.conn.cursor()
        if values:
            await cursor.execute(query, values)
        else:
            await cursor.execute(query)
        return await cursor.fetchall()

    async def fetch_single_query(self, query: str, values: tuple, return_lastrowid: bool = False):
        cursor = await self.conn.cursor()
        await cursor.execute(query, values)
        if return_lastrowid:
            return cursor.lastrowid
        else:
            return await cursor.fetchone()

    async def init_db(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            due_date DATE
        );
        """
        cursor = await self.conn.cursor()
        await cursor.execute(query)
