import sys

for line in sys.stdin:
    n,d=map(int,line.split())
    if n==0 and d==0:
        break
    print "{} {} / {}".format(n/d,n%d,d)

