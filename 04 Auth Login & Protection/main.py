import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PORT = int(os.getenv("PORT", 3000))

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

class AuthRequest(BaseModel):
    email: str | None = None
    password: str | None = None

@app.get("/")
def root():
    return {"message": "Server running and connected to Supabase"}

#------------------------------------------------------------------
# Sign Up
#------------------------------------------------------------------

@app.post("/auth/signup", status_code=201)
def signup(data: AuthRequest):
    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    response = supabase.auth.sign_up({
        "email": data.email,
        "password": data.password
    })

    return response.user

#---------------------------------------------------------------
# Login
#---------------------------------------------------------------

@app.post("/auth/login")
def login(data: AuthRequest):
    if not data.email or not data.password:
        raise HTTPException(
            status_code=400,
            detail="Email and password are required"
        )

    try:
        response = supabase.auth.sign_in_with_password({
                "email": data.email,
                "password": data.password
            })
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid login credentials"
        )

    return{
        "access_token": response.session.access_token,
        "refresh_token": response.session.refresh_token
    }