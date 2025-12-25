from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr, field_validator

add=FastAPI()

class User(BaseModel):
    first_name : Annotated[str, Query(max_length=10)]
    last_name: Annotated[str, Query(max_length=10)]
    email : EmailStr

    @field_validator("email")
    @classmethod
    def Validate_User(cls, v: str)-> str:
        print("Coming here")
        if not v.endswith("@gmail.com"):
            raise ValueError("Email is invalid")
        print("coming....", "v:",v)
        return v



@add.post("/Create_User/")
def create_user(user: User):
    return {"message" : "User created", "user": user}
    
    


