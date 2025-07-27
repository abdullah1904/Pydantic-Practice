from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    balance: float
    isMarried: bool
    skills: List[str]
    contact: Dict[str, str]

    @model_validator(mode='after')
    def validatePhoneContact(cls,model):
        if model.age > 60 and 'phone' not in model.contact:
            raise ValueError("Phone contact is required for users over 60 years old")
        return model
        

def insertUser(user: User):
    print(f"Inserting user: {user.name}, Age: {user.age}, Married: {user.isMarried}, Balance: {user.balance}")
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
    "balance": 1000.50,
    "isMarried": False,
    "skills": ["Python", "Pydantic", "FastAPI"],
    "contact": {
        "phone": "123-456-7890",
        "cell": "987-654-3210",
    }
}

user = User(**user_info)
insertUser(user)