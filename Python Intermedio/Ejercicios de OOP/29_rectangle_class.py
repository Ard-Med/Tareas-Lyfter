# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado


class Rectangle:
    def __init__(self, height, width):
        if height < 0 or width < 0:
            raise ValueError("Negative numbers are invalid. Enter positive numbers only.")
        self.height = height
        self.width = width


    def get_area(self):
        area = self.height * self.width
        return f"The area is: {area}"


    def get_perimeter(self):
        perimeter = (self.height + self.width) * 2
        return f"The perimeter is {perimeter}"

def main ():
    try:
        height = float(input("Enter the height: "))
        width = float(input("Enter the width: "))
        rectangle_info = Rectangle(height, width)
        print(rectangle_info.get_area())
        print(rectangle_info.get_perimeter())
    except ValueError as e:
        print (e)

main()