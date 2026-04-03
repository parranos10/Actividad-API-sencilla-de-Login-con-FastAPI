from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field
from typing import Optional
app = FastAPI()

class User(SQLModel):
    username: str
    password: str

db_users = [
    User(username="admin", password="admin"),
    User(username="user", password="user"),
    User(username="guest", password="guest")
]

@app.get("/")
def read_root():
    return{"Hello":"world"}

@app.post("/login")
def login(user_login: User):
    for u in db_users:
        if u.username == user_login.username and u.password == user_login.password:
            return {"status": "success", "message": f"Bienvenido {u.username}"}
        
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")