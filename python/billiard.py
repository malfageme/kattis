import sys
from math import acos,degrees

for line in sys.stdin:
    a,b,s,m,n=map(int,line.split())
    if a==b==s==m==n==0:
        break
    x=m*a
    y=n*b
    distance=(y**2 + x**2)**(1.0/2)
    speed=distance/s

    angle=degrees(acos(x/distance))
    print "{:.2f} {:.2f}".format(angle, speed)
