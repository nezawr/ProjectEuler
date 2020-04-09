# 10001st prime


""" What is the 10001st prime number ?"""

import random


def check_prime(n):
    num_checks = 300

    check_list = [2, 3, 5, 7, 11, 13, 17, 19]

    if n in check_list:
        return True
    for i in range(num_checks):  # Fermat's Little Theorem
        random_num = random.randint(2, n - 1)
        if pow(random_num, n - 1, n) != 1:
            return False
    else:
        return True


def prime_sum(n):

    check_list = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in range(20,n):
        if check_prime(i):
            check_list.append(i)
    return sum(check_list)


def find_prime(n):
    check_list = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 20
    while len(check_list) != n:
        if check_prime(i):
            check_list.append(i)
        i += 1
    return check_list[-1]


print(prime_sum(2000000))
print(find_prime(10001))

