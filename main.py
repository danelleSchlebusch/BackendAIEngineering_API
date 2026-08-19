#-------------------------------------------------------------------
#Initialization
#-------------------------------------------------------------------

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
import os
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}

#------------------------------------------------------------------
#Create Database
#------------------------------------------------------------------

def init_db():
    connection = psycopg.connect(**DB_CONFIG)

    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (" \
    "id SERIAL PRIMARY KEY," \
    "title TEXT NOT NULL," \
    "done BOOLEAN NOT NULL)")

    cursor.execute("SELECT COUNT(*) FROM tasks")

    count = cursor.fetchone()[0]

    if count == 0:
        cursor.executemany("INSERT INTO tasks (title, done) VALUES (%s, %s)",
                           [
                               ("LearnFast API", False),
                               ("Build CRUD API", False),
                               ("Connect SQLite Database", False)
                           ])
        
    connection.commit()
    connection.close()

init_db()

#------------------------------------------------------------------
#Opening the database
#------------------------------------------------------------------

def get_db_connection():
    return psycopg.connect(**DB_CONFIG, row_factory = dict_row)

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
def get_tasks(search: str | None = None, done: bool | None = None, sort: str | None = None):
    connection = get_db_connection()

    query = "SELECT * FROM tasks"
    parameters = []

    if search:
        query += " WHERE title LIKE %s"
        parameters.append(f"%{search}%")

    if done is not None:
        if search:
            query += " AND done = %s"
        else:
            query += " WHERE done = %s"

        parameters.append(done)

    if sort == "title":
        query += " ORDER BY title"

    tasks = connection.execute(query, parameters).fetchall()

    connection.close()

    return tasks

@app.get("/stats", summary = "Display Task Statistics")
def get_stats():
    connection = get_db_connection()

    stats = connection.execute("SELECT " \
    "COUNT(*) AS total, " \
    "COUNT(*) FILTER (WHERE done = TRUE) AS completed, " \
    "COUNT(*) FILTER (WHERE done = FALSE) AS pending " \
    "FROM tasks").fetchone()

    connection.close()
    return dict(stats)

@app.get("/tasks/{task_id}", summary = "Display a Task")
def get_task(task_id: int):
    connection = get_db_connection()
    task = connection.execute("SELECT * FROM tasks WHERE id = %s",
                              (task_id,)).fetchone()

    connection.close()

    if task is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    return task

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

    cursor = connection.execute("INSERT INTO tasks (title, done) VALUES (%s, %s) RETURNING id", 
                                (task.title, False))

    connection.commit()

    task_id = cursor.fetchone()["id"]
    new_task = connection.execute("SELECT * FROM tasks WHERE id = %s", (task_id,)).fetchone()

    connection.close()
    return new_task
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

    cursor = connection.execute("UPDATE tasks SET title = %s, done = %s WHERE id = %s",
                                (updated_task.title, updated_task.done, task_id))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    connection.commit()

    updated_task = connection.execute("SELECT * FROM tasks WHERE id = %s", (task_id,)).fetchone()

    connection.close()
    return updated_task


@app.delete("/tasks/{task_id}", status_code=204, summary = "Delete a Task")
def delete_task(task_id: int):
    connection = get_db_connection()

    cursor = connection.execute("DELETE FROM tasks WHERE id = %s", (task_id,))

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code = 404,
            detail = f"Task {task_id} not found"
        )

    connection.commit()
    connection.close()
    return Response(status_code = 204)