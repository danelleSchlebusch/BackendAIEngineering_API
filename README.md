# CRUD Task API

A RESTful CRUD API built with **FastAPI, Python, PostgreSQL, and Docker Compose** as part of a Backend AI Engineering learning project.

The API demonstrates the complete Create, Read, Update, and Delete (CRUD) cycle using PostgreSQL as the database and Docker Compose to run the API and database together.

---

## Features

* Create tasks
* Retrieve all tasks
* Retrieve a task by ID
* Update tasks
* Delete tasks
* Search tasks by title
* Filter tasks by completion status
* Sort tasks by title
* View task statistics
* Health check endpoint
* Interactive Swagger API documentation
* PostgreSQL database integration
* Automatic table creation
* Three seeded tasks
* Docker Compose one-command startup

---

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* PostgreSQL
* psycopg
* Docker
* Docker Compose

---

## Project Structure

```text
.
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── compose.yml
├── database.py
├── main.py
└── README.md
```

`.env` contains the local database connection configuration and is ignored by Git.

`.env.example` is committed to the repository as a template.

---

## Environment Variables

The application uses the following environment variable:

| Variable       | Description                  | Example                                 |
| -------------- | ---------------------------- | ---------------------------------------- |
| `DATABASE_URL` | PostgreSQL connection string | `postgres://postgres:dev@db:5432/tasks` |

The repository contains `.env.example` with the required configuration.

Create your local `.env` file from the example before starting the application:

```bash
cp .env.example .env
```

**Do not commit `.env` to GitHub.** It may contain credentials.

---

## Run the Application

The entire API and PostgreSQL database can be started with one command.

### 1. Clone the repository

```bash
git clone https://github.com/danelleSchlebusch/BackendAIEngineering_API.git
```

### 2. Navigate to the project

```bash
cd BackendAIEngineering_API
```

### 3. Create the environment file

```bash
cp .env.example .env
```

### 4. Start the complete stack

```bash
docker compose up
```

Docker Compose starts:

* The FastAPI application
* The PostgreSQL database
* The database health check
* The API after PostgreSQL is ready

No manual database or table creation is required.

The API is available at:

```text
http://localhost:3000
```

---

## Clean Clone Checkpoint

A fresh clone should work without any manual database setup.

Run:

```bash
cp .env.example .env
docker compose up
```

Once the containers are running, test:

```bash
curl -i http://localhost:3000/tasks
```

The API should return the three seeded tasks:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Build CRUD API",
    "done": false
  },
  {
    "id": 3,
    "title": "Connect PostgreSQL Database",
    "done": false
  }
]
```

This confirms that a stranger can clone the repository, configure `.env`, run `docker compose up`, and use the API without manually setting up PostgreSQL.

---

## API Documentation

### Swagger UI

Once the application is running:

```text
http://localhost:3000/docs
```

### ReDoc

```text
http://localhost:3000/redoc
```

---

## API Endpoints

| Method | Endpoint           | Description                           |
| ------ | ------------------ | -------------------------------------- |
| GET    | `/`                | Returns API information               |
| GET    | `/health`          | Health check                          |
| GET    | `/about`           | Returns author and course information |
| GET    | `/tasks`           | Retrieve tasks                        |
| GET    | `/tasks/{task_id}` | Retrieve a task by ID                 |
| GET    | `/stats`           | Retrieve task statistics              |
| POST   | `/tasks`           | Create a new task                     |
| PUT    | `/tasks/{task_id}` | Update an existing task               |
| DELETE | `/tasks/{task_id}` | Delete a task                         |

### GET `/tasks` Query Parameters

The `/tasks` endpoint supports optional query parameters:

| Parameter | Description                 | Example                 |
| --------- | ---------------------------- | ------------------------ |
| `search`  | Search task titles          | `/tasks?search=FastAPI` |
| `done`    | Filter by completion status | `/tasks?done=false`     |
| `sort`    | Sort tasks by title         | `/tasks?sort=title`     |

Parameters can also be combined:

```text
/tasks?search=API&done=false&sort=title
```

---

## Example Request

The following request retrieves all tasks:

```bash
curl -i http://localhost:3000/tasks
```

Example response:

```text
HTTP/1.1 200 OK
content-type: application/json

[{"id":1,"title":"Learn FastAPI","done":false},{"id":2,"title":"Build CRUD API","done":false},{"id":3,"title":"Connect PostgreSQL Database","done":false}]
```

---

## Database

The application uses **PostgreSQL** running as a Docker Compose service.

The database service is named:

```text
db
```

The PostgreSQL database is named:

```text
tasks
```

The application waits for PostgreSQL to become healthy before starting the API.

The `tasks` table is created automatically by the application when it starts.

The table structure is:

| Column  | Type    | Description       |
| ------- | ------- | ------------------ |
| `id`    | SERIAL  | Primary key       |
| `title` | TEXT    | Task title        |
| `done`  | BOOLEAN | Completion status |

---

## Seeded Data

When the `tasks` table is empty, the application automatically creates three tasks:

1. Learn FastAPI
2. Build CRUD API
3. Connect PostgreSQL Database

The seeded data can be verified using PostgreSQL:

```bash
docker compose exec db psql -U postgres -d tasks
```

Then:

```sql
\dt
```

and:

```sql
SELECT * FROM tasks;
```

---

## Database Screenshot

The following screenshot shows the PostgreSQL `tasks` table and the seeded data using `psql`.

![PostgreSQL Database](database.jpg)

---

## Validation

The API validates task titles when creating and updating tasks.

An empty or whitespace-only title returns:

```text
HTTP 400 Bad Request
```

Requests for a task that does not exist return:

```text
HTTP 404 Not Found
```

Successful task creation returns:

```text
HTTP 201 Created
```

Successful deletion returns:

```text
HTTP 204 No Content
```

---

## Learning Objectives

This project demonstrates how to:

* Build REST APIs using FastAPI
* Create GET, POST, PUT, and DELETE endpoints
* Use path and query parameters
* Use Pydantic models for request validation
* Return JSON responses
* Raise HTTP exceptions
* Perform CRUD operations
* Write SQL queries
* Connect FastAPI to PostgreSQL
* Use psycopg to communicate with PostgreSQL
* Run an API and database using Docker Compose
* Use environment variables for database configuration
* Seed a database automatically
* Test APIs using `curl`
* Test APIs using Swagger UI
* Verify PostgreSQL data using `psql`
* Publish a runnable project to GitHub

---

## Author

**Danelle Schlebusch**

Backend AI Engineering Learning Project