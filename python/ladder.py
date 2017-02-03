import sys
from math import radians, sin, ceil

h,v=map(int,sys.stdin.readline().split())

print int(ceil(h/sin(radians(v))))
