# Number letter counts

S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
H = 7
T = 8

total = 0
for i in range(1, 1000):
    c = i % 10  # singles digit
    b = ((i % 100) - c) / 10  # tens digit
    a = ((i % 1000) - (b * 10) - c) / 100  # hundreds digit

    if a != 0:
        total += S[int(a)] + H  # "S[a] hundred
        if b != 0 or c != 0: total += 3  # "and"
    if b == 0 or b == 1:
        total += S[int(b * 10 + c)]
    else:
        total += D[int(b)] + S[int(c)]

total += S[1] + T


from datetime import *

counter = 0
year = 1901
month = 1

curr_day = date(year,month,1)

while(curr_day.year < 2001):
	if(curr_day.weekday() == 6):
		counter += 1
	if(month+1 == 13):
		month = 1
		year += 1
	else:
		month += 1
	curr_day = date(year,month,1)

print("Counter: " + str(counter))