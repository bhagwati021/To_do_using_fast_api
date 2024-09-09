from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI() #create an instance of FastAPI

#the app instance is the main component of our fastapi application .it is used to configure the application

todos = []  #create an empty list to store todos , in memory db

#the @app.get() decorator is used to define an endpoint

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/todos")
def det_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todos(todo_id: int):
    for todo in todos:
        if todo['id']== todo_id:
            return todo
    return {"error":"Todo not found"}

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict()) #append to do to the list
    return todos[-1]  #return the last todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for todo in todos:
        if todo['id']== todo_id:
            todos.remove(todo)
            return {"message":"todo deleted successfully"}
    return {"error":"todo not found"}


