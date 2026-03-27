# Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if (age <= 4):
    print(f"{name}, You're a {age} year old baby.")
elif (age >= 5 and age <= 10):
    print(f"{name}, You're a {age} year old boy.")
elif (age >= 11 and age <= 12):
    print(f"{name}, You're on the preadolescent range.")
elif (age >= 13 and age <= 20):
    print(f"{name} {last_name}, You're and adolescent.")
elif (age >= 21 and age <= 39):
    print(f"{name} {last_name}, You're officially an adult!")
elif (age >= 40 and age <= 59):
    print(f" Mr. {last_name}, You're a seasoned adult.")
else:
    print(f" Mr. {last_name}, You're a senior adult.")
