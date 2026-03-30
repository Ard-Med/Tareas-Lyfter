# Cree una función que acepte un string con palabras separadas por un guion
# y retorne un string igual pero ordenado alfabéticamente.

def order_strings_alphabeticly(placeholder):
    sorted_string_to_list = sorted(placeholder.split("-"))
    add_hyphen = "-".join(sorted_string_to_list)
    return add_hyphen

string1 = "standing-here-i-realize"
string2 = "al-mich-el-falta-barrio"
print(order_strings_alphabeticly(string2))
