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

userDict = user.model_dump(include=['name','address'], exclude={'address': {'zip_code'}})
userJson = user.model_dump_json()
print(userDict, "type:", type(userDict))
print(userJson, "type:", type(userJson))