# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"


class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak (self):
        return "Makes a sound"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Wuff"


def main ():
    cat = Cat("Luna")
    dog = Dog("Nena")
    print (cat.speak())
    print (dog.speak())

main()