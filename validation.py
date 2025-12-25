from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel

app=FastAPI()

@app.get("/valid1/")


def valid(a):
    if len(a)<3:
        return "reject"
    elif len(a)>10:
        return "Reject"
    else:
        return "Accepted"



