# Auth Login & Protection API

A FastAPI authentication API using Supabase for user registration, login, token verification, and protected routes.

The project demonstrates how to build an authenticated API where users can:

* Create an account
* Log in and receive access and refresh tokens
* Access public API information
* Access protected profile information using a valid Supabase access token
* Access a protected dashboard
* Log out through an authenticated endpoint

## Technologies

* Python
* FastAPI
* Supabase
* Pydantic
* Uvicorn
* python-dotenv

## Project Structure

```text
04 Auth Login & Protection/
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── swagger.jpg
```

> The `.env` file contains private Supabase credentials and is excluded from Git. It must never be committed or pushed to GitHub.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/danelleSchlebusch/BackendAIEngineering_API.git
cd "01 Build your first CRUD API/04 Auth Login & Protection"
```

### 2. Create your environment file

Create a `.env` file using `.env.example` as the template:

```text
SUPABASE_URL=your-supabase-url-here
SUPABASE_KEY=your-supabase-key-here
PORT=3000
```

Replace the placeholder values with your own Supabase project credentials.

### 3. Install dependencies

Create and activate a Python virtual environment if required, then install the project's dependencies.

```bash
pip install fastapi uvicorn supabase python-dotenv pydantic
```

## Run the API

Start the API with:

```bash
uvicorn main:app --reload --port 3000
```

The API will be available at:

```text
http://localhost:3000
```

Interactive Swagger documentation is available at:

```text
http://localhost:3000/docs
```

## API Reference

| Method | Endpoint               | Description                                                       | Authentication |
| ------ | ---------------------- | ----------------------------------------------------------------- | -------------- |
| GET    | `/`                    | Checks that the server is running and connected to Supabase       | No             |
| POST   | `/auth/signup`         | Creates a new user account                                        | No             |
| POST   | `/auth/login`          | Authenticates a user and returns access and refresh tokens        | No             |
| GET    | `/public/info`         | Returns publicly accessible information                           | No             |
| GET    | `/protected/profile`   | Returns the authenticated user's profile                          | **Yes**        |
| POST   | `/auth/logout`         | Logs out an authenticated user                                    | **Yes**        |
| GET    | `/protected/dashboard` | Returns a protected dashboard response for the authenticated user | **Yes**        |

## Authentication

Protected endpoints require a valid Supabase access token.

The token is sent using the HTTP Bearer authentication scheme:

```text
Authorization: Bearer <access_token>
```

The API verifies the token with Supabase before allowing access to protected endpoints.

If a token is missing, invalid, or expired, the API returns an HTTP `401 Unauthorized` response.

## Swagger Documentation

The API can be tested interactively through FastAPI's Swagger UI.

![Swagger UI](images/swagger.jpg)

## Security

Sensitive environment variables are stored in `.env` and are excluded from Git using `.gitignore`.

A `.env.example` file is included in the repository with placeholder values so that another developer can configure their own Supabase credentials without exposing secrets.

**Never commit or share the real `.env` file or Supabase keys.**
