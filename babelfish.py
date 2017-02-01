#!/usr/bin/python

import sys

my_dict={}

line=sys.stdin.readline().split()
while line:
    my_dict[line[1]]=line[0]
    line=sys.stdin.readline().split()

word=sys.stdin.readline().strip()
while word:
    try:
        print my_dict[word]
    except:
        print "eh"
    word=sys.stdin.readline().strip()

