from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from models import ToDoItem, Database

load_dotenv()  # Load environment variables from .env file

app = FastAPI()
db = Database()


@app.post("/todos/")
def create_todo_item(todo_item: ToDoItem):
    query = "INSERT INTO tasks (name, description, due_date) VALUES (%s, %s, %s) RETURNING id;"
    values = (todo_item.name, todo_item.description, todo_item.due_date)
    todo_id = db.fetch_single_query(query, values)[0]
    return {"id": todo_id, **todo_item.dict()}


@app.get("/todos/{todo_id}")
def read_todo_item(todo_id: int):
    query = "SELECT name, description, due_date FROM tasks WHERE id = %s;"
    todo_item = db.fetch_single_query(query, (todo_id,))
    if todo_item is None:
        raise HTTPException(status_code=404, detail="To-Do Item not found")
    return {"id": todo_id, "name": todo_item[0], "description": todo_item[1], "due_date": todo_item[2]}


@app.put("/todos/{todo_id}")
def update_todo_item(todo_id: int, todo_item: ToDoItem):
    query = "UPDATE tasks SET name = %s, description = %s, due_date = %s WHERE id = %s;"
    values = (todo_item.name, todo_item.description,
              todo_item.due_date, todo_id)
    db.execute_query(query, values)
    return {"id": todo_id, **todo_item.dict()}


@app.delete("/todos/{todo_id}")
def delete_todo_item(todo_id: int):
    query = "DELETE FROM tasks WHERE id = %s;"
    db.execute_query(query, (todo_id,))
    return {"message": "To-Do Item deleted successfully"}
