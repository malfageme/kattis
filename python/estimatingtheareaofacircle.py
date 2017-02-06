import sys
from math import pi


for line in sys.stdin:
    r,m,c=map(float,line.split())
    if r==m==c==0:
        break
    print pi*r*r, ((2*r)**2)*c/m
