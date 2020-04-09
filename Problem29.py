# Distinct powers

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

def distinct_pow(a,b):

    lst = []

    for i in range(2,a+1):
        for j in range(2,b+1):
            lst.append(iterated_squaring(i,j))
    return list(set(lst))

print(len(distinct_pow(100,100)))


