
def get_name():
    try:
        name = (input("Enter your name: "))
        if name.isdigit() == True : 
            raise ValueError ()
        return name
    except ValueError as e: 
        print(f"You entered {name} and your name can't be a number")


def get_age():
    try:
        return int(input("Enter your age: "))
    except ValueError as e: 
        print(f"You did not enter a number")
        raise e


while True:
    try:
        print(f"Hello {get_name()}, your age is: {get_age()}")
        break
    except ValueError:
        continue