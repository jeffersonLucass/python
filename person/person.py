class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_Name(self):
        return self.name

    def get_Age(self):
        return self.age
    
    def full_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __str__(self):  
        return f"Name: {self.name}, Age: {self.age}"
