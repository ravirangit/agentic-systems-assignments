from fastapi import FastAPI
import json
from typing import Optional

with open("people.json", "r") as f:
    people = json.load(f)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/search")
async def search_people(name: Optional[str] = None, age: Optional[int] = None):
    """
    Search for people by name and/or age
    Usage: /search?name=Deepak&age=23
    """
    for person in people:
        match = True
        if name and name.lower() not in person["name"].lower():
            match = False
        if age and person["age"] != age:
            match = False
        if match:
            return person
    return {"message": "No matching person found."}