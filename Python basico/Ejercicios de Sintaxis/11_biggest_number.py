# Cree un programa que le pida tres números al usuario y muestre el mayor.

number1 = int(input("Enter the first number: ")) 
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

list_of_numbers = [number1, number2, number3]

print("The biggest number is: ", max(list_of_numbers))

# Adicionalmente encontre esta linea para pedir los 3 numeros en un solo input:
# # Source - https://stackoverflow.com/a/28165771
# Posted by greentec, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-07, License - CC BY-SA 3.0

# a = [int(x) for x in input().split()]

# Pero no entiendo completamente como funciona