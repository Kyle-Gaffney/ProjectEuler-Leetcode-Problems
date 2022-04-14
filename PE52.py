from itertools import count
#import timer
import time
start=time.time()



for x in count(100002 , 3):
    if int(str(x)[0]) < 2:
        if all(sorted(str(x*k)) == sorted(str(x)) for k in range(6,2,-1)):
            # display the time elapsed for solution
            end = time.time()
            print(f"Time elapsed:  {(end - start)}")
            print(x , 2*x , 3*x , 4*x , 5*x , 6*x)
            break

