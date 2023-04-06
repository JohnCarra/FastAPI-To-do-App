import os
import time
from fastapi import FastAPI, HTTPException
from models import ToDoItem, Database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()


@app.on_event("startup")
async def startup_event():
    await db.connect()
    await db.init_db()  # Call the init_db method from the Database class


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.post("/todos")
async def create_todo_item(todo_item: ToDoItem):
    query = "INSERT INTO tasks (name, description, due_date) VALUES (?, ?, ?);"
    values = (todo_item.name, todo_item.description, todo_item.due_date)
    todo_id = await db.fetch_single_query(query, values, return_lastrowid=True)
    return {"id": todo_id, **todo_item.dict()}


@app.get("/todos")
async def read_all_todo_items():
    query = "SELECT id, name, description, due_date FROM tasks;"
    todo_items = await db.fetch_query(query)
    return [{"id": item[0], "name": item[1], "description": item[2], "due_date": item[3]} for item in todo_items]


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
