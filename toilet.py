#!/usr/bin/python

import sys

line=sys.stdin.readline().strip()

start=line[0]
result=["U",start,0],["D",start,0],["",start,0]
for c in line[1:]:
  for case in result:
    # Do we need to set the seat before sitting
    if c!=case[1]:
        case[2]+=1
    case[1]=c
    # Do we need to set the seat before sitting
    if len(case[0])!=0:
        if case[0]!=case[1]:
            case[2]+=1
        # Leave the seat as the policy mandates
        case[1]=case[0]

for case in result:
    print case[2]

