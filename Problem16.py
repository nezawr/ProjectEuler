# Power digit sum

"""215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?"""


def power2(a,b):
    result = 1
    while b>0: # b has more digits
        if b%2 == 1: # b is odd
            result = result*a
        a = a*a
        b = b//2 # discard b's rightmost bit
    return result


def power_digit_sum(x,y):

    result = power2(x,y)
    sum = 0
    for i in str(result):
        sum += int(i)
    return sum


print(power_digit_sum(2,1000))
