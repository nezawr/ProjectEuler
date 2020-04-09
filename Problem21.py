import math


# 4b1
def sum_divisors(n):
    result = 0
    i = 2

    while i <= (math.sqrt(n)):

        if n % i == 0:

            if i == (n / i):
                result = result + i
            else:
                result = result + (i + n / i)
        i = i + 1
    result = result + 1

    return int(result)




# 4d
def is_amicable(n):
    y = sum_divisors(n)
    if sum_divisors(y) == n and y != n:
        return True
    else:
        return False


# 4e
def count_amicable_numbers(limit):

    lst = []

    for i in range(1, limit + 1):
        if is_amicable(i) and sum_divisors(i) not in lst:
            lst.append(i)
    return len(lst)

