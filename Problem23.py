#############
# Problem 23
#############


"""" Non-abundant sums:
     Find the sum of all the positive integers
     which cannot be written as the sum of two
     abundant numbers. """

import math
import itertools


def sum_divisors(n):
    result = 0
    i = 2

    if n == 1:
        return 0

    while i <= (math.sqrt(n)):

        if n % i == 0:

            if i == (n / i):
                result = result + i
            else:
                result = result + (i + n / i)
        i = i + 1
    result = result + 1

    return int(result)

lst_abunds = []
for i in range(1, 28124):
    if sum_divisors(i) > i:
        lst_abunds.append(i)


rock_it = [sum(x) for x in itertools.combinations_with_replacement(lst_abunds,2) if sum(x) < 28124]

rock_it = list(set(rock_it)) # removed duplicates
last_one = [i for i in range(1,28124)]
for i in rock_it:
    last_one.remove(i)
print(sum(last_one))


