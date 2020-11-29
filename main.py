from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import json

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/description/{hostname}")
def read_item(hostname: str, q: Optional[str] = None):
    data = '{"name": "veronica", "description": "laptop" }'
    data_dict = json.loads(data)
    return {data_dict["name"]: data_dict["description"], "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}