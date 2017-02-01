#!/usr/bin/python

import sys

n_friends,n_friendships=map(int, sys.stdin.readline().split())

friends=[]

for i in n_friends:
    friends.append(int(sys.stdin.readline()))

friendships=[]
for i in n_friendships:
    f1,f2=map(int, sys.stdin.readline().split())



