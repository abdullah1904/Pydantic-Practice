from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict

class User(BaseModel):
    name: str
    email: EmailStr
    age: int
    balance: float
    height: float
    weight: float 
    isMarried: bool
    skills: List[str]
    contact: Dict[str, str]
    @computed_field
    @property
    def bmi(self) -> float:
        if self.height <= 0:
            raise ValueError("Height must be greater than zero to calculate BMI")
        bmi = self.weight / ((self.height / 100) ** 2)
        return round(bmi, 2)

def insertUser(user: User):
    print(f"Inserting user: {user.name}, Age: {user.age}, Married: {user.isMarried}, Balance: {user.balance}, BMI: {user.bmi}")
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
    "height": 175.5,
    "weight": 70.0,
    "isMarried": False,
    "skills": ["Python", "Pydantic", "FastAPI"],
    "contact": {
        "phone": "123-456-7890",
        "cell": "987-654-3210",
    }
}

user = User(**user_info)
insertUser(user)