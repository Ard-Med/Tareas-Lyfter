# Cree una función que reciba una lista de palabras y un número n,
# y retorne una nueva lista con solo las palabras que tengan más de n letras

def check_for_minimum_letters (list_of_words, number_treshold):
    over_treshold_list = []
    for word in list_of_words:
        if len(word) >= number_treshold:
            over_treshold_list.append(word)
    return over_treshold_list


list_by_user = input("Enter a list of words: ").split()
treshold_by_user = int(input("Enter the character treshold: "))

print(check_for_minimum_letters(list_by_user, treshold_by_user))