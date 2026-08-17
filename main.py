#-------------------------------------------------------------------
#Initialization
#-------------------------------------------------------------------

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import sqlite3

app = FastAPI()

#------------------------------------------------------------------
#Create Database
#------------------------------------------------------------------

def init_db():
    connection = sqlite3.connect("tasks.db")

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (" \
    "id INTEGER PRIMARY KEY," \
    "title TEXT NOT NULL," \
    "done BOOLEAN NOT NULL)")

    cursor.execute("SELECT COUNT(*) FROM tasks")

    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("INSERT INTO tasks (id, title, done) VALUES (?, ?, ?)",
                           [
                               (1, "LearnFast API", False),
                               (2, "Build CRUD API", False),
                               (3, "Connect SQLite Database", False)
                           ])
        
    connection.commit()
    connection.close()

init_db()

#------------------------------------------------------------------
#Opening the database
#------------------------------------------------------------------

def get_db_connection():
    connection = sqlite3.connect("tasks.db")
    connection.row_factory = sqlite3.Row
    return connection

#------------------------------------------------------------------
#Stage 1: Your first real endpoint
#------------------------------------------------------------------

@app.get("/", summary = "API Information")
def root():
    return{
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health", summary = "Health Check")
def health():
    return{
        "status": "ok"
    }

@app.get("/about", summary = "Personal Information")
def about():
    return{
        "author": "Danelle",
        "course": "CRUD API"
    }

#-----------------------------------------------------------------
#Stage 2: Read: list and a single task
#-----------------------------------------------------------------

@app.get("/tasks", summary = "Display Tasks")
def get_tasks():
    connection = get_db_connection()
    tasks = connection.execute("SELECT * FROM tasks").fetchall()

    connection.close()

    return [dict(task) for task in tasks]

@app.get("/tasks/{task_id}", summary = "Display a Task")
def get_task(task_id: int):
    connection = get_db_connection()
    task = connection.execute("SELECT * FROM tasks WHERE id = ?",
                              (task_id,)).fetchone()

    connection.close()

    if task is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    return dict(task)

#---------------------------------------------------------
#Stage 3 - Create: POST a new task
#---------------------------------------------------------

class TaskCreate(BaseModel):
    title: str

@app.post("/tasks", status_code=201, summary = "Create a New Task")
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(
            status_code = 400,
            detail = "Title cannot be empty"
        )

    connection = get_db_connection()

    cursor = connection.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (task.title, False))

    connection.commit()

    task_id = cursor.lastrowid
    new_task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    connection.close()
    return dict(new_task)
#---------------------------------------------------------------
#Stage 4 - Update and Delete
#---------------------------------------------------------------

class TaskUpdate(BaseModel):
    title: str
    done: bool

@app.put("/tasks/{task_id}", summary = "Update a Task")
def update_task(task_id: int, updated_task: TaskUpdate):
    if not updated_task.title.strip():
        raise HTTPException(
            status_code = 400,
            detail = "Title cannot be empty"
        )

    connection = get_db_connection()

    cursor = connection.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?",
                                (updated_task.title, updated_task.done, task_id))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    connection.commit()

    updated_task = connection.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()

    connection.close()
    return dict(updated_task)


@app.delete("/tasks/{task_id}", status_code=204, summary = "Delete a Task")
def delete_task(task_id: int):
    connection = get_db_connection()

    cursor = connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    connection.commit()
    connection.close()
    return Response(status_code = 204)