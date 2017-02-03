import sys

cost=float(sys.stdin.readline())
num_lawns=int(sys.stdin.readline())

total=0
for _ in range(num_lawns):
    w,l=map(float,sys.stdin.readline().split())

    total+=cost*w*l

print total
