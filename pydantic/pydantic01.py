from pydantic import BaseModel, Field, validators,field_validator

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    
    @field_validator('zip_code')
    def validate_zip_code(cls, value):
        if len(value) != 5 or not value.isdigit():
            raise ValueError('Zip code must be a 5-digit number')
        return value
    
    @field_validator('state')
    def validate_state(cls, value):
        if len(value) != 2:
            raise ValueError('State must be a 2-letter code')
        return value.upper()
    
class Customer(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=50)
    email: str
    alias: str = ...
    address : Address
    
    @field_validator('alias')
    def validate_alias(cls, value):
        if len(value) < 10 or len(value) > 20:
            raise ValueError('Alias must be between 10 and 20 characters')
        return value

customer = {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "alias": "john doe XX", "address": {"street": "123 Main St", "city": "Anytown", "state": "CA", "zip_code": "12345"}}

print(customer)
# print(customer.alias)
# print(customer.model_dump())
# print(customer.model_dump_json())
# print(customer.model_dump_json(indent=2))

customer_info = Customer(**customer)
print(customer_info)