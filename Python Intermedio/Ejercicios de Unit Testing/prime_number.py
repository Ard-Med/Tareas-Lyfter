
def check_for_prime_number(placeholder):
    prime_number_list = []
    not_prime = []
    for each_number in placeholder:
        is_prime = True
        for divisor in range(2, each_number):
            if each_number % divisor == 0:
                is_prime = False
        if is_prime:
            prime_number_list.append(each_number)
        else:
            not_prime.append(each_number)
    print(f"prime: {prime_number_list} not prime: {not_prime}")

if __name__ == "__main__":
    list_by_user = [int(number) for number in input("Enter a few numbers to know which one is prime: ").split()]
    check_for_prime_number(list_by_user)