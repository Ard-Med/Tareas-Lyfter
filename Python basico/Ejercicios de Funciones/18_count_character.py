# Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto.

def count_character (text_to_check, letter_to_count):
    return text_to_check.count(letter_to_count)

string1 = input("Enter a string: ")
string2 = input("Enter the character you want to count: ")

print(f"The character was found {count_character(string1, string2)} times.")


# def count_character (placeholder, placeholder2):
#     for each_letter in placeholder:
#         characters = placeholder.count(placeholder2)
#         return characters 

# string1 = input("Enter a string: ")
# string2 = input("Enter the character you want to count: ")

# print(count_character(string1, string2))