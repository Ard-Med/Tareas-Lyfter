# Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.


def numbers_only(func):
    def wrapper (*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(f"Only numbers are allowed, got {arg}")
        return func(*args)
    return wrapper

@numbers_only
def main(entered_value):
    print(f"You entered the number: {entered_value}")

main(5)
main("hi")