from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()


class Validate(BaseModel):
    input : str

@app.post("/valid3/")
def Valid(i: Validate):
    print("saurabh is here", type(i))
    print(i)

    if len(i.input)>10 or len(i.input)<2:
        return "invalid"

    else:
        return "Valid"



