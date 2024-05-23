from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/")
def create_item(item: Item):
    return item
