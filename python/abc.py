import sys

num=sorted(map(int,sys.stdin.readline().split()))
order=sys.stdin.readline().strip()

print " ".join([str(num[ord(c)-ord('A')]) for c in order])
