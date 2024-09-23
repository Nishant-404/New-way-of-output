import random
import time
import os
alp = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',"r","s","t","u","v","w","x","y","z"]
al = []
wor = input("Enter a word")
j = len(wor)
i= 0
a = []
while True:
    
    n = random.randint(0,26)
    a.append(alp[n])
    for k in a:
        time.sleep(.02)
        print(k,end = "")
        os.system('cls')
    print()
    
    if i == j:
        break
    elif wor[i]==alp[n]:
        i+=1
        continue 
        
    else:
        a.pop()