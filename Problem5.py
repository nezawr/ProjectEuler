# Sum square difference

"""Find the difference between the sum of the
squares of the first one hundred natural numbers and the square of the sum."""


def find_difference(n):
    sum1 = 0
    sum2 = 0

    for i in range(1, n + 1):
        sum1 += i ** 2
        sum2 += i
    sum2 = sum2 ** 2

    return sum2 - sum1


print(find_difference(100))


def rec_factors(n, start = 2):

    while n % start != 0 and n > start:
        start += 1

    if start > n:
        return []
    else:
        return [start] + rec_factors(n//start,start)




ans = (5 < 6 < 7)
print(ans)