# Iterated squaring helper function.
def pow(x, n):
    r = 1
    while n:
        if n % 2 == 1:
            r *= x
            n -= 1
        x *= x
        n /= 2
    return r

def sum_pow(n):
    result = 0
    for i in range(1,n+1):
        result += pow(i,i)
    return result

print(sum_pow(1000))
