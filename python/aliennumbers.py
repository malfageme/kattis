#!/usr/bin/python

import sys

num_cases=int(sys.stdin.readline())

default_base="0123456789abcdefghijklmnopqrstuvwxyz"

def int_from_base(num, source):
    base=len(source)
    res=0
    for i in range(len(num)):
        rad=len(source)**i
        res+=rad*int(source.index(num[len(num)-1-i]))
    return res

def int_to_base(num, target):
    res=""
    base=len(target)
    while 1:
        remainder=num%base
        res=target[remainder] + res
        num=num/base
        if num==0:
            break
    return res

for i in range(num_cases):
    num, source, target=sys.stdin.readline().split()
    num_int=int_from_base(num, source)
    print "Case #{}: {}".format(i+1,int_to_base(num_int, target))


