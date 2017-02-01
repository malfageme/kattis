#!/usr/bin/python

import sys

num_samples=int(sys.stdin.readline())

samples=map(int, sys.stdin.readline().split())

print len([x for x in samples if x<0])
