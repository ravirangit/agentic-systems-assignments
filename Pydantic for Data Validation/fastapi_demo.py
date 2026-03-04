from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# localhost:8000/welcome
@app.get("/welcome")
def read_root():
    return {"Hello": "World"}