#project Euler problem 3
x=600851475143
i=1
factors=[]
while True:
    i+=1
    if x % i ==0:
        factors.append(i)
        if x == i:
            break
        x = x / i
        i=1
print(factors)
print("PE 3 solution:" , max(factors))
