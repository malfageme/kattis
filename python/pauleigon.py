import sys

n,p,q=map(int, sys.stdin.readline().split())

print 'opponent' if ((p+q)/n % 2) else 'paul'
