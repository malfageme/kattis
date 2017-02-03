import sys
from math import sin,cos,radians

num_cases=int(sys.stdin.readline())

g=9.8

for line in sys.stdin:
    v,a,x,h1,h2=map(float,line.split())
    t=x/(v*cos(radians(a)))
    y=v*t*sin(radians(a)) - g*t*t/2
    if y<h1 or y>h2 or min(map(abs,[y-h1,y-h2]))<1:
        print "Not Safe"
    else:
        print "Safe"
