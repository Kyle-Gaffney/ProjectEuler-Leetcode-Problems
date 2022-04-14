from collections import Counter
import math

solutionfactors=[2,2,5]
i=1
for x in range(19,7,-1):
    xfactors=[]
    while True:
        i+=1
        if x % i == 0:
            xfactors.append(i)
            if x == i:
                i=1
                break
            x = x / i
            i=1
    factordiff = list((Counter(xfactors) - Counter(solutionfactors)).elements())
    solutionfactors.extend(factordiff)

print(solutionfactors)
print('the solution to project Euler problem 4 is:' , math.prod(solutionfactors))

# yields the elements in `list_2` that are NOT in `list_1`