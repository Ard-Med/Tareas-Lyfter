# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

list1 = [1,2,3,4,5]

list1[0], list1[-1] = list1[-1], list1[0]
print(list1)