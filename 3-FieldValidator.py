from pydantic import BaseModel, EmailStr,field_validator
from typing import List, Dict

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    balance: float
    isMarried: bool
    skills: List[str]
    contact: Dict[str, str]
    @field_validator('email', mode='before')
    @classmethod
    def validateEmail(cls, value):
        valid_domains = ["uet.pk", "entspos.com"]
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain '{domain_name}' is not allowed. Allowed domains: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name', mode='after')
    @classmethod 
    def transformName(cls, value):
        return value.upper()
    @field_validator('age', mode='after')
    @classmethod
    def validateAge(cls, value):
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        return value

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
    "email": "john.doe@entspos.com",
    "age": 30,
    "balance": 1000.50,
    "isMarried": True,
    "skills": ["Python", "Pydantic"],
    "contact": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
}

user = User(**user_info)
insertUser(user)