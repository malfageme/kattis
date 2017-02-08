import sys

num_cases=int(sys.stdin.readline())
for i in range(num_cases):
    num_stores=int(sys.stdin.readline())
    pos_stores=map(int,sys.stdin.readline().split())
    print 2*(max(pos_stores)-min(pos_stores))

