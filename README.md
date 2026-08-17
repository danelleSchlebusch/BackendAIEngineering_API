# CRUD Task API

A simple RESTful CRUD API built with **FastAPI** and **Python** as part of a Backend AI Engineering learning project.

This API demonstrates the basic Create, Read, Update, and Delete (CRUD) operations using an in-memory list of tasks.

---

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Health check endpoint
- Interactive Swagger API documentation

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/danelleSchlebusch/BackendAIEngineering_API.git
```

### 2. Navigate to the project folder

```bash
cd BackendAIEngineering_API.git
```

### 3. Install the required packages

```bash
pip install fastapi uvicorn
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

You should see output similar to:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## API Documentation

Once the server is running, open your browser and navigate to:

Swagger UI

```
http://127.0.0.1:8000/docs
```

Alternative ReDoc documentation

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Returns API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Retrieve all tasks |
| GET | `/tasks/{task_id}` | Retrieve a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## Example Task

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## Example Response

### GET `/tasks`

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false
  },
  {
    "id": 2,
    "title": "Build CRUD API",
    "completed": true
  }
]
```

---

## Project Structure

```text
.
├── main.py
├── README.md
└── .gitignore
```

---

## Swagger Screenshot

After running the application, take a screenshot of the Swagger UI (`/docs`) and save it inside your project, for example:

```
images_swagger.jpg
```

Then display it below.

```markdown
![Swagger UI](images_swagger.jpg)
```

---

## Learning Objectives

This project demonstrates how to:

- Build REST APIs using FastAPI
- Create API endpoints
- Handle path parameters
- Use Pydantic models for request validation
- Return JSON responses
- Raise HTTP exceptions
- Test APIs using Swagger UI
- Publish a project to GitHub

---
## Explored SQLite

### SQL Query

```sql
DELETE FROM tasks 
WHERE id = 5;
```

This query deleted the row from tasks where the id was equal to 5.

---

## Author

**Danelle Schlebusch**

Backend AI Engineering Learning Project