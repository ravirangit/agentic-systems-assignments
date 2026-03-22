from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    username: str = Field(..., description="The username of the user", max_length=30)
    email: str = Field(..., description="The email address of the user")
    age: int = Field(..., description="The age of the user", ge=18, le=120)

    @field_validator('email')
    def validate_email(cls, value):
        if value.split('@')[-1] != 'example.com':
            raise ValueError('Invalid domain, only example.com is allowed')
        return value
    
user_info = {'username': 'john_doe', 'email': 'john@ehh.com', 'age': 25}

user = User(**user_info)
print(user)