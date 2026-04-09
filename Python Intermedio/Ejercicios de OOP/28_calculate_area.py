# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.

import math

class Circle:
    radius = 0
    def get_area(self,radius):
        area = math.pi*(radius**2)
        return area

my_circle = Circle()
print(my_circle.get_area(1))