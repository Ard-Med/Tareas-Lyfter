# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

string1 = "print me backwards"

for i in range(len(string1) - 1, -1, -1):
    print(string1[i])