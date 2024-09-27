from abc import ABC, abstractmethod

# Classe abstraite Animal
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass

# Sous-classe Dog qui hérite de Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"

# Sous-classe Cat qui hérite de Animal
class Cat(Animal):
    
    def sound(self):
        return "Meow"

# Test des sous-classes
if __name__ == "__main__":
    dog = Dog()
    print(dog.sound())  # Affiche "Bark"

    cat = Cat()
    print(cat.sound())  # Affiche "Meow"

