#!/usr/bin/python

import sys

num_cases=int(sys.stdin.readline())


for _ in range(num_cases):
    recording=sys.stdin.readline().split()
    while len(recording)==0:
        recording=sys.stdin.readline().split()
    other=[]
    verb="goes"
    while verb!="does":
        new_animal=sys.stdin.readline().split()
        verb=new_animal[1]
        if verb=="goes":
            other.extend(new_animal[2::])
    fox_says=[x for x in recording if x not in other]
    print " ".join(fox_says)


