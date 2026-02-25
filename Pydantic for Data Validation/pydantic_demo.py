from pydantic import BaseModel, ValidationError, Field

class Student(BaseModel):
    name: str
    age: int = Field(..., gt=0, description="Age must be a positive integer")
    email: str
    
student_info = {
    "name": "Alice",
    "age": 20,
    "email": "alice@example.com"
}

student_info = {
    "name": "Bob",
    "age": 10,
    "email": "bob@example.com"
}
student1 = Student(**student_info)
print(student1)