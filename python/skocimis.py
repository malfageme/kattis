import sys

a,b,c=map(int,sys.stdin.readline().split())

max_holes=max(b-a,c-b)-1
print max_holes
#print ((max_holes/2)+1)

