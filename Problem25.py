# 1000-digit Fibonacci number

"""What is the index of the first term
in the Fibonacci sequence to contain 1000 digits?"""


prev = 1
curr = 1
i = 2

while len(str(curr)) != 1000:
    prev, curr = curr, prev + curr
    i += 1
print(i)



