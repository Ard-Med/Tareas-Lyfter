# Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total

def sum_values (list_from_user):
    total_sum = 0
    for each_value in list_from_user:
        try:
            float_value = float(each_value)
            total_sum += float_value
            print(f"{float_value} was additioned correctly")
        except ValueError:
            print(f"Value {each_value} is not a number")
    return total_sum


test_list = ["1", "13", "apoco si?", "puro tronco", "26.78", "3.169"]

print(f"The total sum is: {sum_values(test_list)}")