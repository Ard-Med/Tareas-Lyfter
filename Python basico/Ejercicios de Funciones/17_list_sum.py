def calculate_sum_of_numbers (sum_of_numbers):
    return sum(sum_of_numbers)

    
list_by_user = [int(i) for i in input("Enter a list of numbers to see their sum: ").split()]

print(calculate_sum_of_numbers(list_by_user))