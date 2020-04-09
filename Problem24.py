########
#Permutations
########

from itertools import permutations


perms = [''.join(p) for p in permutations('0123456789')]
sorted = sorted(perms)
print(sorted[999999])


