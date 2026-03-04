from pydantic import BaseModel, Field, ValidationError, field_validator

class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(min_length=6, max_length=6) # Regular expression to ensure 6-digit pincode

class User(BaseModel):
    user_id: int 
    name: str
    email: str
    age: int = Field(..., ge=18)  # Age must be greater than 18
    address: Address
    is_premium: bool
    

user_info = {
    "user_id": 1,
    "name": "John Doe",
    "email": "hello@gmail.com",
    "age": 18,
    "address": {
        "city": "New York",
        "pincode": "123456"
    },
    "is_premium": True
}

# ** -> unpacking. 
user = User(**user_info)
print(user)
