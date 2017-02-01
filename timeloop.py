#!/usr/bin/python

import sys

try:
  max = int(sys.stdin.read())
except:
  exit(0)
   

for i in range(1,max+1):
  print "{} Abracadabra".format(i)

