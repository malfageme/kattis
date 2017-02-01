#!/usr/bin/python

import sys

max_problems, max_time=map(int, sys.stdin.readline().split())

a,b,c,t0=map(int, sys.stdin.readline().split())


t=[t0]

for i in range(1,max_problems):
    t.append(((a*t[i-1]+b)%c)+1)

print t

t=sorted(t)

print t

spent_time=0
solved=0
penalty=0
while spent_time<max_time and solved<max_problems:
    spent_time+=t[solved]
    if spent_time>max_time:
        break
    penalty=(penalty + spent_time) % 1000000007
    solved+=1

print solved, penalty

exit(0)
