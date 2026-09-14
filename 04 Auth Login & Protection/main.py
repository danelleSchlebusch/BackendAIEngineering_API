import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from supabase import create_client, Client

load_dotenv()
security = HTTPBearer()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
PORT = int(os.getenv("PORT", 3000))

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        response = supabase.auth.get_user(token)
        return response.user
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


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

#--------------------------------------------------------------------
#Public Route
#--------------------------------------------------------------------

@app.get("/public/info")
def public_info():
    return{
        "message": "Welcome stranger! This info is public."
    }

#------------------------------------------------------------------
#Protected Route
#------------------------------------------------------------------

@app.get("/protected/profile")
def protected_profile(user = Depends(get_current_user)):
    return{
        "id": user.id,
        "email": user.email,
        "account_created": user.created_at
    }

#------------------------------------------------------------------
#Logout
#------------------------------------------------------------------

@app.post("/auth/logout", status_code=204)
def logout(user = Depends(get_current_user)):
    supabase.auth.sign_out()
    return None

#-----------------------------------------------------------------
#Protected Dashboard
#-----------------------------------------------------------------

@app.get("/protected/dashboard")
def protected_dashboard(user = Depends(get_current_user)):
    return{
        "message": "Welcome to your protect dashboard",
        "user_id": user.id
    }