filename = "euler13.txt"

with open(filename,"r") as ans:

    lst1 = []
    for line in ans:
        lst1.append(line)


lst2 = []

for i in lst1:
    lst2.append(int(i))

needed_sum = sum(lst2)
print(str(needed_sum)[0:10])