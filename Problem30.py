# Digit fifth powers.
# Concept: Narcissictic numbers.

def iterated_squaring(a,b):

    result = 1

    while b > 0:
        if b % 2 == 1:
            result = result * a
            b = b - 1
        else:
            a = a * a
            b = b//2

    return result





lst = []
for i in range(2,1000000):
    str1 = str(i)
    sum1 = 0
    for digit in str1:
        sum1 += (int(digit))**5
    if sum1 == i:
        lst.append(i)
print(sum(lst))
