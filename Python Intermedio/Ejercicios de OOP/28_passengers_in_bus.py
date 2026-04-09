# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).
import random

class Person:
    def __init__(self, number):
        self.number = number

class Bus:
    def __init__(self, max_passengers):
        self.current_passengers = []
        self.max_passengers = max_passengers

    def get_person_on_bus(self, person):
        if len(self.current_passengers) >= self.max_passengers:
            print("The bus is full!")
            return
        self.current_passengers.append(person)
        print(f"{person.number} got on the bus!")

    def get_person_off_bus(self):
        if not self.current_passengers:
            print("The bus is empty!")
            return
        removed = self.current_passengers.pop(random.randrange(len(self.current_passengers)))
        print(f"{removed.number} got off the bus")


def main():
    my_bus = Bus(max_passengers=25)
    people = [Person(str(i)) for i in range(1, 28)]

    for person in people:
        my_bus.get_person_on_bus(person)

    for _ in range(len(my_bus.current_passengers)):
        my_bus.get_person_off_bus()

main()