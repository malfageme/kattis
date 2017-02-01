#!/usr/bin/python

import sys

x,y,n=map(int,sys.stdin.readline().split())

for i in range(1,n+1): 
    msg="Fizz" if i%x==0 else ""
    msg+="Buzz" if i%y==0 else ""
    print (msg if len(msg) else i)
