# Cree una clase de User que:
# Tenga un atributo de date_of_birth.
# Tenga un property de age.
# Luego cree un decorador para funciones que acepten un User como parámetro 
# que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = date.today()
        age =  today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
        


def check_age(func):
    def wrapper(user):
        if user.age <18:
            raise ValueError("User is underage!")
        return func(user)
    return wrapper

@check_age
def main(user):
    print(f"Welcome! your age is {user.age}")

adult = User(date(1990, 1, 1))
minor = User(date(2015, 1, 1))

main(adult)
main(minor)