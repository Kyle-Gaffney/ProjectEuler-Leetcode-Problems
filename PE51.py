def get_primes(n):
  m = n+1
  #numbers = [True for i in range(m)]
  numbers = [True] * m #EDIT: faster
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range(2, m):
    if numbers[i]:
      primes.append(i)
  return primes

primeslist=get_primes(10**7)
l6=[x for x in primeslist if len(str(x))==6]
def fourcombo():
    binresults=[]
    for i in range(1,16):
        binresults.append('{0:04b}'.format(i))
    return binresults
def fivecombo():
    binresults=[]
    for i in range(1,32):
        binresults.append('{0:05b}'.format(i))
    return binresults

for i in l6:
    prime=str(i)
#prime='121313'
    family=[]
    for j in fourcombo():
        tempfamily=[]
        for k in range(10):
            primetest=prime[0]
            position=1
            for m in j:
                if m=='1':
                    primetest+=str(k)
                elif m=='0':
                    primetest+=prime[position]
                position+=1
            primetest+=prime[5]
            if int(primetest) in l6:
                tempfamily.append(primetest)
                if len(tempfamily)==8:
                    print(tempfamily)
                    break
        family.append(tempfamily)
    for j in fivecombo():
        tempfamily=[]
        for k in range(10):
            primetest=''
            position=0
            for m in j:
                if m=='1':
                    primetest+=str(k)
                elif m=='0':
                    primetest+=prime[position]
                position+=1
            primetest+=prime[5]
            if int(primetest) in l6:
                tempfamily.append(primetest)
                if len(tempfamily)==8:
                    print(tempfamily)
                    break
        family.append(tempfamily)

lengths=[len(x) for x in family]
print(max(lengths))

#This works but is SLOOOOWWWW