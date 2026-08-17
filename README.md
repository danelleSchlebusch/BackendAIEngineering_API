# CRUD Task API

A simple RESTful CRUD API built with **FastAPI, Python,** and **SQLite** as part of a Backend AI Engineering learning project.

This API demonstrates the basic **Create, Read, Update, and Delete (CRUD)** operations using a SQLite database.

---

## Features

- Create a new task
- Retrieve all tasks
- Retrieve a task by ID
- Update an existing task
- Delete a task
- Health check endpoint
- Interactive Swagger API documentation
- SQLite database integration
- Automatic database and table creation
- Three seeded tasks when the database is created for the first time

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic
- SQLite

---

## Database

### Why SQLite?

SQLite was chosen for this project because it is lightweight and does not require a separate database server or additional database setup.

The database is stored as a single file called:

```
tasks.db
```

The application automatically creates the database when it starts if it does not already exist.

It also automatically creates the tasks table and adds three example tasks when the table is empty.

This means that someone can clone the repository and start the application without manually creating the database or table.

### Database Location

The tasks.db file is created in the main project directory:

```text
.
├── main.py
├── README.md
├── .gitignore
└── tasks.db
```

The database file is included in .gitignore, so it is not committed to GitHub.

This means that when someone clones the repository, their own tasks.db will be created automatically when they start the application.

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
The application will automatically create tasks.db, create the tasks table, and add the three seeded tasks if the database does not already contain any tasks.

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
| GET | `/about` | Returns author and course information |
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

The application initially seeds the database with:

1. LearnFast API
2. Build CRUD API
3. Connect SQLite Database

---

## Example Response

### GET `/tasks`

```json
[ 
  { 
    "id": 1, 
    "title": "LearnFast API", 
    "done": false 
  }, 
  { 
    "id": 2, 
    "title": "Build CRUD API", 
    "done": false 
  }, 
  { 
    "id": 3, 
    "title": "Connect SQLite Database", 
    "done": false 
  } 
]
```

---

## Database Screenshot

The SQLite database can be viewed using DB Browser for SQLite.

The screenshot below shows the tasks table and its seeded tasks.

Save the screenshot in the project directory, for example:

```
database_screenshot.jpg
```

Then display it here:

```markdown
![SQLite Database](database_screenshot.jpg)
```

---

## Example SQL Query

The following SQL query was used during Stage 4 to delete a task with a specific ID:

```sql
DELETE FROM tasks 
WHERE id = 5;
```

This query deleted the row from tasks table where the id was equal to 5.

Another useful query for viewing all tasks is:

```sql
SELECT * FROM tasks;
```

---

## Automatic Database Creation

The database is created automatically when main.py starts.

The application:

1. Connects to tasks.db.
2. Creates the tasks table if it does not already exist.
3. Checks whether the table contains any tasks.
4. Adds three seeded tasks if the table is empty.
5. Commits the changes and closes the database connection.

This allows the project to work from a clean clone without requiring manual database setup.

## Clean Clone Test

To verify that the database is created automatically:

1. Delete tasks.db from the project directory.
2. Start the application using:
```bash
uvicorn main:app --reload
```
3. The application should automatically recreate tasks.db.
4. Open:
```
http://127.0.0.1:8000/tasks
```
5. The three seeded tasks should be returned.

This confirms that the database setup works automatically.
---

## Project Structure

```text
.
├── main.py
├── README.md
├── .gitignore
├── database_screenshot.png
└── tasks.db
```

```text
tasks.db is created automatically and is ignored by Git, so it will not be included in the GitHub repository.
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
- Perform Create, Read, Update, and Delete operations
- Connect FastAPI to a SQLite database
- Create a SQLite database automatically
- Seed a database with initial data
- Execute SQL queries
- Test APIs using Swagger UI
- View a SQLite database using DB Browser for SQLite
- Publish a project to GitHub

---

## Author

**Danelle Schlebusch**

Backend AI Engineering Learning Project