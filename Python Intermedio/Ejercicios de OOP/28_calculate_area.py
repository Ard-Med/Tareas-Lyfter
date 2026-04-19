# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = math.pi*(self.radius**2)
        return area

my_circle = Circle()
print(my_circle.get_area(1))