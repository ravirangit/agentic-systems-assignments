import json
from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

def load_students_data():
    # Load students data from students.json file.
    with open('students.json', 'r') as f:
        students_data = json.load(f)

    return students_data

# localhost:8000/welcome
# http://127.0.0.1:8000/docs
@app.get("/welcome")
async def root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/students/{student_id}")
def get_student_with_id(student_id: str = Path(..., description="Id of the student which you want to access.", examples="STU-1001")):
    data = load_students_data()
    # find the student with the given id in the data
    for student in data:
        if student["student_id"] == student_id:
            return student
    
    raise HTTPException(status_code=404, detail="Student not found.")

@app.get("/students")
def get_all_students():
    data = load_students_data()
    return data