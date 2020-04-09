# Special Pythagorean triplet

"""There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

for i in range(1,1000):
    for j in range(1,i):
        x = i**2 + j**2
        y = (1000 - i - j)**2
        if x == y:
            c = 1000 - i - j
            print("The triplet is {} and their product is {}".format((j,i,c),i*j*c))

