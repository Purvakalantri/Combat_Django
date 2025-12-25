from typing import Union
from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI()

@app.get("/users/")

def Hello():
    return "hello worldd"

