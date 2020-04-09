#Circular Primes

import random
from itertools import permutations



def check_prime(n):
    num_checks = 300

    check_list = [2, 3, 5, 7, 11]

    if n in check_list:
        return True
    for i in range(num_checks):  # Fermat's Little Theorem
        random_num = random.randint(2, n - 1)
        if pow(random_num, n - 1, n) != 1:
            return False
    else:
        return True



def rotation(n):
  rotations = set()
  for i in range(len(str(n))):
    m = int(str(n)[i:] + str(n)[:i])
    rotations.add(m)
  return rotations


def circular_prime(n):

    for i in rotation(n):
        if check_prime(i) != True:
            return False
    return True

print(circular_prime(20))



