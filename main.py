import os
import time
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from models import ToDoItem, Database

load_dotenv()  # Load environment variables from .env file

app = FastAPI()
db = Database()


async def wait_for_db():
    while True:
        try:
            await db.connect()
            break
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            time.sleep(5)  # Wait for 5 seconds before trying again


@app.on_event("startup")
async def startup():
    await wait_for_db()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.post("/todos/")
async def create_todo_item(todo_item: ToDoItem):
    query = "INSERT INTO tasks (name, description, due_date) VALUES ($1, $2, $3) RETURNING id;"
    values = (todo_item.name, todo_item.description, todo_item.due_date)
    todo_id = await db.fetch_single_query(query, values)
    return {"id": todo_id[0], **todo_item.dict()}


@app.get("/todos/{todo_id}")
async def read_todo_item(todo_id: int):
    query = "SELECT name, description, due_date FROM tasks WHERE id = $1;"
    todo_item = await db.fetch_single_query(query, (todo_id,))
    if todo_item is None:
        raise HTTPException(status_code=404, detail="To-Do Item not found")
    return {"id": todo_id, "name": todo_item[0], "description": todo_item[1], "due_date": todo_item[2]}


@app.put("/todos/{todo_id}")
async def update_todo_item(todo_id: int, todo_item: ToDoItem):
    query = "UPDATE tasks SET name = $1, description = $2, due_date = $3 WHERE id = $4;"
    values = (todo_item.name, todo_item.description,
              todo_item.due_date, todo_id)
    await db.execute_query(query, values)
    return {"id": todo_id, **todo_item.dict()}


@app.delete("/todos/{todo_id}")
async def delete_todo_item(todo_id: int):
    query = "DELETE FROM tasks WHERE id = $1;"
    await db.execute_query(query, (todo_id,))
    return {"message": "To-Do Item deleted successfully"}
