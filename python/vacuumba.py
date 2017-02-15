import sys
from math import radians,degrees,cos,sin

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    num_segments=int(sys.stdin.readline())
    pos=[0,0]
    angle=0
    for _ in range(num_segments):
        a,d=map(float, sys.stdin.readline().split())
        angle+=a
        pos[0]+=d*sin(-1*radians(angle))
        pos[1]+=d*cos(-1*radians(angle))

    print pos[0], pos[1]
