#Python code solution to Project Euler problem 2
fn = [1,1]
i=1
result=0
while True:
    fn.append(fn[i]+fn[i-1])
    i+=1
    if fn[i]>4*10**6:
        break
    elif i % 3 == 2 :
        result+=fn[i]
print(result)
