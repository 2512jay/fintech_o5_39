class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")


# Create an instance of the Person class
person = Person("Alice", 25)

# Access attributes
print(person.name)
print(person.age)

# Call methods
person.greet()
