# Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.

def count_cased_letters (placeholder):
    upper_cases = 0
    lower_cases = 0
    for each_letter in placeholder:
        if each_letter.isupper() == True:
            upper_cases = upper_cases + 1
        elif each_letter.islower():
            lower_cases = lower_cases + 1
    return(f"There are {upper_cases} Uppercase letters and {lower_cases} lower case letters")

string1 = "HoW MaNy LeTteRs Of EaCh TyPe"

print(count_cased_letters(string1))