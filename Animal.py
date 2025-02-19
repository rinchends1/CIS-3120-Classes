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
        print(f"Happy Birthday! I am now {self.__age} years old, and {self.__color} in color")



