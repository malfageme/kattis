import sys

for line in sys.stdin:
    n=int(line)
  
    if n==1:
        print 1
    else: 
     
        res=1
        c=1
        while res!=0:
            res = (res*10 + 1) % n
            c+=1
        print c
