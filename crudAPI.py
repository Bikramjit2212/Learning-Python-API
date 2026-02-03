from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import os

from dotenv import load_dotenv
load_dotenv()

print(os.getenv("FOO2"))

# create an instance of fast api
app = FastAPI()

todos = [] #create an empty list to store todos, in memeory db

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/todos")
def get_todos():
    return todos 

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.model_dump()) #append todo to list
    return todos[-1] #return the last todo
    # new_todo = todo.model_dump()
    # todos.append(new_todo)
    # return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    return{"error": "Todo not found.."}


