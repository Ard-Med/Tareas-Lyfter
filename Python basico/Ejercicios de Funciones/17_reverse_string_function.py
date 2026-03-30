# Cree una función que le dé la vuelta a un string y lo retorne.

def return_function (string_to_be_reversed):
    reversed_string = ""
    for reversed_letter in range(len(string_to_be_reversed) - 1, -1, -1):
        reversed_string += string_to_be_reversed[reversed_letter]
    return reversed_string


string1 = "you were just like me, trying to make history"

print(return_function(string1))

