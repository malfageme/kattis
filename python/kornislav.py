import sys

steps=sorted(map(int,sys.stdin.readline().split()), reverse=True)

print steps[1]*steps[3]
