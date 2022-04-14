from math import comb
print(comb(23,10), comb(23,11), comb(23,12), comb(23,13))
solution=4
for x in range(24,101):
    i=3
    while comb(x,i)<10**6:
        i+=1
    if x % 2 == 0:
        solution += 2 * (x / 2 - i) + 1
    elif x % 2 == 1:
        solution += 2 * ((x + 1) / 2 - i)
print(solution)
