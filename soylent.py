import sys
from math import ceil


num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    cal=int(sys.stdin.readline())
    print int(ceil(cal/400.0))
