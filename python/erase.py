import sys

n=int(sys.stdin.readline())%2
f_b=map(int,sys.stdin.readline().strip())
f_a=map(int,sys.stdin.readline().strip())

print 'Deletion', 'succeeded' if all([(f_a[i]^f_b[i])==n for i in range(len(f_b))]) else 'failed'
