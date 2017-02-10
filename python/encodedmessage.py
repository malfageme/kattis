import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    pt=sys.stdin.readline().strip()
    n=int(len(pt)**(1.0/2))
    matrix=[pt[i*n:i*n+n] for i in range(n)]
    print "".join(["".join(row) for row in zip(*[row[::-1] for row in matrix])])

