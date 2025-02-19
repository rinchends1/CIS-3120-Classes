class Animal:
    def __init__(self, name, species, age, color): 
        self.__name = name
        self.__species = species
        self.__age = age
        self.__color = color
        print(f"Hello, I am {self.__name}, a {self.__species}.")

    def talk(self):
        print("Hi")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name
        print(f"My new name is {self.__name}")

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_color(self): 
        return self.__color

    def birthday(self):
        self.__age += 1
        print(f"Happy Birthday! I am now {self.__age} years old, and I am {self.__color} in color.")

    def describe(self):
        print(f"My name is {self.__name}, I am a {self.__color} {self.__species}, and I am {self.__age} years old.")

# Subclasses for specific animals
class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, "Dog", age, color)
        self.__breed = breed

    def talk(self):
        print("Woof! Woof!")

    def get_breed(self):
        return self.__breed

class Cat(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, "Cat", age, color)
        self.__breed = breed

    def talk(self):
        print("Meow! Meow!")

    def get_breed(self):
        return self.__breed

class Bird(Animal):
    def __init__(self, name, age, color, species, can_fly=True):
        super().__init__(name, species, age, color)
        self.__can_fly = can_fly

    def talk(self):
        print("Chirp! Chirp!")

    def fly(self):
        if self.__can_fly:
            print(f"{self.get_name()} is flying!")
        else:
            print(f"{self.get_name()} can't fly.")

# Testing the classes
if __name__ == "__main__":
    dog = Dog("Buddy", 3, "Brown", "Labrador")
    dog.describe()
    dog.talk()
    print(f"Breed: {dog.get_breed()}")
    dog.birthday()

    cat = Cat("Whiskers", 2, "White", "Persian")
    cat.describe()
    cat.talk()
    print(f"Breed: {cat.get_breed()}")
    cat.birthday()

    parrot = Bird("Polly", 1, "Green", "Parrot")
    parrot.describe()
    parrot.talk()
    parrot.fly()