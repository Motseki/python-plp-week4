class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print a message introducing the person
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Lebohang Motseki", 30, "Male")

# Call the introduce method
person1.introduce()
