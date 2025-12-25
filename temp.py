from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app=FastAPI()

class Item(BaseModel):
    item_id : int
    item_name : str  

@app.post("/item/")
def Fun(item: Item):
    return item #or you can just return {item.item_id, item.item_name}

