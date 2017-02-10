import sys

num_cases=int(sys.stdin.readline())

sl=0
t=0
for _ in range(num_cases):
    m,s=map(int,sys.stdin.readline().split())
    sl+=m
    t+=s

print float(t)/(sl*60)
