from pydantic import BaseModel, Field

class Student(BaseModel):
    name: str = Field(..., description="The name of the student", max_length=50)
    age: int = Field(..., description="The age of the student", ge=5, le=100)
    grade: str = Field(..., description="The grade of the student")
    
student1 = {"name": "Alice", "age": 1, "grade": "A"}
student2 = {"name": "Bob", "age": 22, "grade": "B"}

student1_obj = Student(**student1)
student2_obj = Student(**student2)
print(student1_obj)
print(student2_obj)