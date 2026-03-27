# Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás

def transform_to_int (entered_values):
        for each_value in entered_values:
            try:
                int_value = int(each_value)
                print(f" '{each_value}' was transformed into {int_value}")
            except ValueError: 
                print(f"Value {each_value} is not a number")


list_of_data = ["1", "2", "3", "f", "4"]

transform_to_int(list_of_data)
