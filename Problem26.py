#Cyclic Fractions.

def is_prime(n):

    i = 2

    while i*i <= n:
        if n%i == 0:
            return False
        i += 1


    return True


def find_primes_below(n):

    lst = []
    for i in range(n,1,-1):
        if is_prime(i):
            lst.append(i)
    return lst



for p in find_primes_below(1000):
    c = 1
    while pow(10,c,p) != 1:
        c +=1
    if p - c == 1:
        break
print(p)


