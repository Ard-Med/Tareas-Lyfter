# Cree un decorador que haga print de los parámetros y retorno de la función que decore.


def my_decorator(func):
    def wrapper (*args):
        print(f"My decorator is printing my function arguments: {args}")
        print("This is inside a decorator")
        result = func(*args)
        print(f"My decorator is printing the return value: {result}")
        return result
    return wrapper

@my_decorator
def main(parameter1):
    print("This is inside a function")
    return (f"I received {parameter1}")

main("test")