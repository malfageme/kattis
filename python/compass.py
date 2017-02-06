import sys

n1=int(sys.stdin.readline())
n2=int(sys.stdin.readline())

n12=720+n1-n2
n21=720+n2-n1

if (n12%360) < (n21%360):
    print (n12%360) * (1 if n12<0 else -1)
else:
    print (n21%360) * (-1 if n21<0 else 1)

