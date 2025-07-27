from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address = Address(
    street="123 Main St",
    city="Anytown",
    state="CA",
    zip_code="12345"
)

user = User(
    name="John Doe",
    age=30,
    gender="male",
    address=address
)

print(user)