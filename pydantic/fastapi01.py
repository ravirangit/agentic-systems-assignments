from fastapi import FastAPI

app = FastAPI()
items = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_name}")
def get_item(item_name: str):
    if item_name in items:
        return {f"item_name": item_name}
    else:
        return {"error": "Item not found"}

@app.post("/items")
def create_item(item_name: str):
    items.append(item_name)
    return items