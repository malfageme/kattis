#!/usr/bin/python

import sys

n,m=map(int,sys.stdin.readline().split())

res={}

for i_n in range(1,n+1):
    for i_m in range(1,m+1):
        try:
            res[i_n+i_m]+=1
        except:
            res[i_n+i_m]=1

max_sum=max(res.values())

for i in res.items():
    if i[1]==max_sum:
        print i[0]

