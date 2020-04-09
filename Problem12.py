# Highly divisible triangular number

""" What is the value of the first triangle
number to have over five hundred divisors?"""

def divisors(n):

    result = [1,n]
    i = 2


    while i <= (n)**0.5:

        if n % i == 0:
            if i == (n/i):
                result.append(i)
            else:
                result.append(i)
                result.append(int(n/i))
        i = i + 1
    return len(result)


def triangle(n):
    result = 0
    for i in range(1,n+1):
        result += i
    return result


def limit(n):

    i = 1
    while divisors(triangle(i)) < n:
        i += 1
    return triangle(i)

print(limit(500))