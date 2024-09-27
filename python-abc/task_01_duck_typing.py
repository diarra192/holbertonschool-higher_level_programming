from abc import ABC, abstractmethod
import math

# Classe abstraite Shape
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def circumference(self):
        pass

# Classe Circle qui hérite de Shape
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius

# Classe Rectangle qui hérite de Shape
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return 2 * (self.width + self.height)

# Fonction shape_info qui accepte n'importe quel objet respectant l'interface Shape
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Circumference: {shape.circumference()}")

# Test avec un cercle et un rectangle
if __name__ == "__main__":
    circle = Circle(5)
    print("Circle Info:")
    shape_info(circle)  # Affiche l'aire et le périmètre du cercle

    print("\nRectangle Info:")
    rectangle = Rectangle(4, 6)
    shape_info(rectangle)  # Affiche l'aire et le périmètre du rectangle

