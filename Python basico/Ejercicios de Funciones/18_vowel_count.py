# Cree una función que reciba un string y retorne cuántas vocales contiene

def count_vowels(string_to_count):
    vowels = "aeiouAEIOU"
    vowel_counter = 0
    for letter in string_to_count:
        if letter in vowels:
            vowel_counter = vowel_counter + 1
    return vowel_counter

string_by_user = input("Enter a word to check how many vowels it has: ")
print(f"your word has {count_vowels(string_by_user)} vowels.")