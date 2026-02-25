from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    grade: str
    
student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
student = Student(**student_info)
print(student)