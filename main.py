from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Define database connection details
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

# Define the To-Do Item model


class ToDoItem(BaseModel):
    name: str
    description: str
    due_date: str

# Define the endpoints for creating, reading, updating, and deleting To-Do Items


@app.post("/todos/")
def create_todo_item(todo_item: ToDoItem):
    cursor = conn.cursor()
    query = "INSERT INTO tasks (name, description, due_date) VALUES (%s, %s, %s) RETURNING id;"
    values = (todo_item.name, todo_item.description, todo_item.due_date)
    cursor.execute(query, values)
    todo_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    return {"id": todo_id, **todo_item.dict()}


@app.get("/todos/{todo_id}")
def read_todo_item(todo_id: int):
    cursor = conn.cursor()
    query = "SELECT name, description, due_date FROM tasks WHERE id = %s;"
    cursor.execute(query, (todo_id,))
    todo_item = cursor.fetchone()
    cursor.close()
    if todo_item is None:
        raise HTTPException(status_code=404, detail="To-Do Item not found")
    return {"id": todo_id, "name": todo_item[0], "description": todo_item[1], "due_date": todo_item[2]}


@app.put("/todos/{todo_id}")
def update_todo_item(todo_id: int, todo_item: ToDoItem):
    cursor = conn.cursor()
    query = "UPDATE tasks SET name = %s, description = %s, due_date = %s WHERE id = %s;"
    values = (todo_item.name, todo_item.description,
              todo_item.due_date, todo_id)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return {"id": todo_id, **todo_item.dict()}


@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE id = %s;"
    cursor.execute(query, (todo_id,))
    conn.commit()
    cursor.close()
    return {"message": "To-Do Item deleted successfully"}
