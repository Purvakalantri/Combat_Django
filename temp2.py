from typing import Union
from fastapi import FastAPI, Body

app=FastAPI()
@app.post("/item2/")

def fun2(item: str = Body(...)):
    return {"Recieved text": item}

