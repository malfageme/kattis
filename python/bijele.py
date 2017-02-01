#!/usr/bin/python

import sys, operator

correct_set=[1,1,2,2,2,8]
entry=map(int, sys.stdin.readline().split())

print " ".join(map(str, [i-j for i,j in zip(correct_set,entry)]))
#print " ".join(map(str, map(operator.sub, correct_set, entry)))

