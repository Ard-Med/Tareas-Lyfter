# Cree un programa que elimine todos los números impares de una lista.

number_list = [1,2,3,4,5,6,7,8,9,10] 
only_pairs = []
for number in number_list:
    if number % 2 == 0:
        only_pairs.append(number)
print(only_pairs)
