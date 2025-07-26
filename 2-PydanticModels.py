from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class User(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=50, title="User Name", description="The name of the user", examples=["John Doe", "Jane Smith"], strict=True)]
    email: EmailStr
    age: Annotated[int, Field(gt=0, lt=120, strict=True)]
    married: Annotated[bool, Field(default=False, title="Marital Status", description="Indicates if the user is married", examples=[True], strict=True)]
    balance: Annotated[float, Field(ge=0.0, strict=True)]
    skills: Annotated[List[str], Field(max_length=10, min_length=1, strict=True)]
    contact: Annotated[Dict[str, str], Field(description="User's contact information", strict=True)]
    address: Annotated[Optional[str], Field(description="User's address", default=None, strict=True)]
    portfolio: Annotated[AnyUrl, Field(description="User's portfolio URL")]

def insertUser(user: User):
    print(f"Inserting user: {user.name}, Age: {user.age}, Married: {user.married}, Balance: {user.balance}, Address: {user.address}")
    print(f"Skills:")
    for skill in user.skills:
        print(f"  {skill}")
    print(f"Contact Info:")
    for key, value in user.contact.items():
        print(f"  {key}: {value}")

def updateUser(user: User):
    print(f"Updating user: {user.name}, Age: {user.age}, Married: {user.married}, Balance: {user.balance}, Address: {user.address}")
    print(f"Skills:")
    for skill in user.skills:
        print(f"  {skill}")
    print(f"Contact Info:")
    for key, value in user.contact.items():
        print(f"  {key}: {value}")

user_info = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30,
    "married": True,
    "balance": 1000.50,
    "skills": ["Python", "Pydantic"],
    "contact": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "address": "123 Main St, Anytown, USA",
    "portfolio": "https://johnsportfolio.com"
}

user = User(**user_info)
insertUser(user)
updateUser(user)