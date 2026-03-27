# Cree un programa que cree un diccionario usando dos listas del mismo tamaño.
# Usando una para sus keys, y la otra para sus values.

list_a = ["first_name", "last_name", "role"]
list_b = ["Ard", "Medina", "SRE"]
dictionary = {}

for i in range(len(list_a)):
    dictionary[list_a[i]] = list_b[i]

for key , value in dictionary.items():
    print(key,":", value)
