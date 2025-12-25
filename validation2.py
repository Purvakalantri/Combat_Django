from typing import Union
from fastapi import  FastAPI, Body
from pydantic import BaseModel

app=FastAPI()

@app.post("/valid2/")


# class Valid(BaseModel):
#     a1: int

def is_Valid(a: str= Body(...) ):
    if len(a)>10 or len(a)<=2:
        return "Invalid"
    else:
        return "Valid"