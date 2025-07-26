def insertUser(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age cannot be negative")
        print(f"Inserting user: {name}, Age: {age}")
    else:
        raise TypeError("Invalid types for name or age")

insertUser("John Doe", 10)