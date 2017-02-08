import sys

n,t=map(int,sys.stdin.readline().split())
tasks=map(int, sys.stdin.readline().split())

num_tasks=0
time=0
for i in range(len(tasks)):
    if time+tasks[i]>t:
        print i
        break
    time+=tasks[i]
else:
    print len(tasks)
