import math

def palindrome(product):
    productstring=str(product)
    i=len(productstring)
    result=False
    j=0
    while productstring[j]==productstring[i-1-j]:
        if j>=i//2:
            result=True
            break
        j+=1
    return result

pds=[]
for i in range(999,99,-1):
    for j in range(i,99,-1):
        product=i*j
        if palindrome(product):
            pds.append(product)

print(max(pds))

