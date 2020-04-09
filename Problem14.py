def collatz_seq(n):
    counter = 1
    while n != 1:
        if n % 2 ==0:
            n = n/2
        elif n % 2 ==1:
            n = (3*n) + 1
        counter += 1
    return counter


def collatz_limit(x):

    max_length = 1
    num = 0

    for i in range(1,x):
        if collatz_seq(i) > max_length:
            max_length = collatz_seq(i)
            num = i

    return num,max_length

print(collatz_limit(1000000))