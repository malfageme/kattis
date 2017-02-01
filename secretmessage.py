#!/usr/bin/python

import sys

squares=[x*x for x in range(1,101)]

def doSecretMessage(msg):
    l=len(msg)
    square_index=0
    for x in range(100):
        if squares[x] >= l:
            square_index=x
            break
    len_row=square_index+1
    matrix=[["*" for _ in range(len_row)] for _ in range(len_row)]
    for i in range(l):
        matrix[i/len_row][i%len_row]=msg[i]
    print "".join([x for row in zip(*matrix) for x in row[::-1]]).replace("*","")
    



num_msg=int(sys.stdin.readline())

for i in range(num_msg):
    msg=sys.stdin.readline().strip()
    doSecretMessage(msg)


