class Pet:
    """A class modeling a generic building."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getDescription(self):
        description = f"{self.name} is {self.age}"
        print(description)


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.colot = color

    def speak():
        print(f"my name is {self.name}")


class Dog(Pet):
    def speak():
        print("houuu")
