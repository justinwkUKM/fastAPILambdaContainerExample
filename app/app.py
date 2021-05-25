# IMPORTS
from fastapi import FastAPI, Request
from mangum import Mangum
from typing import Optional
from pydantic import BaseModel
import uvicorn


# BASE MODEL
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# APP OBJECT
app = FastAPI(
    title="HelloWorldAPI",
    version=0.1,
    root_path="/dev/"
)


# METHODS
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1")
async def root():
    return {"message": "Hello World to API V1"}


@app.get("/get_root_path")
def read_main(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


@app.post("/api/v1/items")
def create_item(item: Item):
    item.price = item.price + (item.price * 0.2)
    return item


handler = Mangum(app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
