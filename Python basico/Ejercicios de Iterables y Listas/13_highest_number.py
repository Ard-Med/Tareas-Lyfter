# Cree un programa que le pida al usuario 10 números,
# y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto

int_list = [int(number) for number in input("Enter 10 numbers: ").split()]

print(f"the numbers you entered are: {int_list} and the largest number is: {(max(int_list))}")