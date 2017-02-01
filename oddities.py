#!/usr/bin/python

import sys

cases=int(sys.stdin.readline())

for case in range(cases):
    num=int(sys.stdin.readline())
    print "{} ".format(num) + ("is even" if num%2==0 else "is odd")

