from fastapi import FastAPI
import json

app = FastAPI()

def loan_students():
    with open('student.json', 'r') as f:
        students = json.load(f)
    return students

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students")
async def get_students():
    students = loan_students()
    return students