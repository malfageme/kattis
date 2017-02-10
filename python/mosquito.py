import sys

for line in sys.stdin:
    m,p,l,e,r,s,n=map(int, line.split())
    for i in range(n):
        old_m=m
        m=p/s
        p=l/r
        l=old_m*e
        
    print m
