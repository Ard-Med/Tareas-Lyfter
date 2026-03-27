# Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.

# Esta es mi solucion, la IA me dio la solucion de abajo cuando pregunte una manera de no volver a declarar las variables en el else
# Pero no entiendo bien como esta funcionando la linea 29

import random

random_number = random.randint(1, 10)
guessed_number = int(input("Guess a number from 1 to 10: "))

while (guessed_number != random_number):
    
    if (guessed_number < 1 or guessed_number > 10):
        print("Invalid number, enter a number from 1 to 10")
        break
    else:
        print("So close. The number was ", random_number)
        random_number = random.randint(1, 10)
        guessed_number = int(input("Guess a number from 1 to 10: "))
        
print("You got it! It was", random_number)


#
# import random

# random_number = random.randint(1, 10)

# while True:
#    guessed_number = int(input("Guess a number from 1 to 10: "))
    
#    if guessed_number < 1 or guessed_number > 10:
#        print("Invalid number, enter a number from 1 to 10")
#    elif guessed_number == random_number:
#        print("You got it!")
#        break
#    else:
#        print("So close. The number was", random_number)