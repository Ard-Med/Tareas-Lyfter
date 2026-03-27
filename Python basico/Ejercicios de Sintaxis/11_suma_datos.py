# Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.

string1 = "text1"
string2 = "text2"
int1 = 13
list1 = [1,"word", True]
list2 = [2, "letter", False]
float1 = 3.14169
bool1 = True
bool2 = False

string_sum = string1 + string2
print("this is a sum of strings: ", string_sum)

# string_and_int_sum = string1 + int1
# TypeError: can only concatenate str (not "int") to str

# int_and_string_sum = int1 + string
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

list_and_list_sum = list1 + list2
print(f"This is a sum of lists: {list_and_list_sum}")

# string_and_list_sum = string4 + list1
# TypeError: can only concatenate str (not "list") to str

float_and_int_sum = float1 + int1
print("This is a sum of a float and an int: ", float_and_int_sum)

bool_and_bool_sum = bool1 + bool2
print(f"This is the sum of bools: {bool_and_bool_sum}")