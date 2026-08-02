# Analice el algoritmo de bubble_sort usando la Big O Notation.
# Analice los siguientes algoritmos usando la Big O Notation:


# print_numbers_times_2
def print_numbers_times_2(numbers_list): # O(n)
    for number in numbers_list:  # O(n) - iterates n times
        print(number * 2)        # O(1) - constant operation


# check_if_lists_have_an_equal
def check_if_lists_have_an_equal(list_a, list_b): #O(n²)
    for element_a in list_a:            # O(n) - iterates N times
        for element_b in list_b:        # O(n²) - second nested loop
            if element_a == element_b:  # O(1) - no loops or recursion
                return True             # O(1) - no loops or recursion
    return False                        # O(1) - no loops or recursion


# print_10_or_less_elements
def print_10_or_less_elements(list_to_print): # O(1)
    list_len = len(list_to_print)           # O(1) - constant operation
    for index in range(min(list_len, 10)):  # O(1) - at most 10 iterations
        print(list_to_print[index])         # O(1) - constant operation


# generate_list_trios
def generate_list_trios(list_a, list_b, list_c): # O(n³)
    result_list = []                                          # O(1) - no loops or recursion
    for element_a in list_a:                                  # O(n) - iterates N times
        for element_b in list_b:                              # O(n²) - second nested loop
            for element_c in list_c:                          # O(n³) - third nested loop
                result_list.append(f'{element_a} {element_b} {element_c}')  # O(1) - no loops or recursion
    return result_list                                        # O(1) - no loops or recursion