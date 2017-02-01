#!/usr/bin/python

import sys

line=sys.stdin.readline()
while line:
    num_ops=int(line)
    data_stack=[]
    data_queue=[]
    data_pqueue=[]
    res_stack=[]
    res_queue=[]
    res_pqueue=[]
    res_guess=[]
    for i in range(num_ops):
        op,num=map(int,sys.stdin.readline().split())
        if op==1:
            data_stack.append(num)
            data_queue.append(num)
            data_pqueue.append(num)
        elif op==2:
            try:
                res_stack.append(data_stack.pop())
                res_queue.append(data_queue.pop(0))
                max_pqueue=max(data_pqueue)
                res_pqueue.append(max_pqueue)
                data_pqueue.remove(max_pqueue)
            except:
                pass
            res_guess.append(num)
    msg="impossible"
    if res_stack==res_guess:
        msg="stack"
    if res_queue==res_guess:
        msg="queue" if msg=="impossible" else "not sure"
    if res_pqueue==res_guess:
        msg="priority queue" if msg=="impossible" else "not sure"
    line=sys.stdin.readline()
    print msg


