# Cree una calculadora por linea de comando. 
# Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual.
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.


def addition (actual_number, user_number):
    addition = actual_number + user_number
    print(f"{actual_number} + {user_number} = {addition}")
    actual_number = addition
    return actual_number 


def substraction (actual_number, user_number):
    reduce = actual_number - user_number
    print(f"{actual_number} - {user_number} = {reduce}")
    actual_number = reduce
    return actual_number


def multiplication (actual_number, user_number):
    multiply = actual_number * user_number
    print(f"{actual_number} * {user_number} = {multiply}")
    actual_number = multiply
    return actual_number


def division (actual_number,  user_number):
    try:
        divide = actual_number / user_number
        print(f"{actual_number} / {user_number} = {divide}")
        actual_number = divide
    except ZeroDivisionError as e:
        print(f"Error [ZeroDivisionError]: Division by 0 is invalid: {e}")
    return actual_number


def remove_score (actual_number, user_number = None):
    actual_number = 0 
    print("actual number has been reset back to 0")
    return actual_number


def enter_operator():
    try:
        operation = int(input(
            """Enter the operation you want to do:
            1. addition
            2. substraction
            3. multiplication
            4. division
            5. delete results
            6. exit
            """))
        if operation not in [1,2,3,4,5,6]: 
            raise ValueError ()
    except ValueError as e: 
        print(f"Invalid entry of operator")
        raise e
    return operation


def enter_number():
    try:
        return float(input("Enter a number: "))
    except ValueError as e: 
        print(f"You did not enter a number")
        raise e


def calculator(actual_number, operator, user_number):
    operations = {
        1: addition,
        2: substraction,
        3: multiplication,
        4: division,
        5: remove_score
    }
    return operations[operator](actual_number, user_number)

def run_program ():
    actual_number = 0
    while True:
        try:    
            operator = enter_operator()
            if operator == 6:
                break
            elif operator == 5:
                actual_number = calculator(actual_number, operator, None)
            else:
                actual_number = calculator(actual_number, operator, enter_number())
            print(f"The actual number is: {actual_number}")
        except ValueError:
            continue


run_program()