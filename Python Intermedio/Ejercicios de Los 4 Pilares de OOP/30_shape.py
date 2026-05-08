from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return f"The area is {area}"
    
    
    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return f"The perimeter is {perimeter}"

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    
    def calculate_area(self):
        area = self.side ** 2
        return f"The area is {area}"
    
    
    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return f"The perimeter is {perimeter}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        area = self.width * self.height
        return f"The area is {area}"
    
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return f"The perimeter is {perimeter}"

def main():
    my_circle = Circle(5)        
    my_square = Square(4)
    my_rectangle = Rectangle(5, 6)

    print(my_circle.calculate_area())
    print(my_circle.calculate_perimeter())
    print(my_square.calculate_area())
    print(my_square.calculate_perimeter())
    print(my_rectangle.calculate_area())
    print(my_rectangle.calculate_perimeter())
    
main()