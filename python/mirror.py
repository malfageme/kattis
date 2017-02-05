import sys

num_cases=int(sys.stdin.readline())

for i in range(1,num_cases+1):
    r, c=map(int, sys.stdin.readline().split())
    d=[]
    for _ in range(r):
        d.append(sys.stdin.readline().strip())
    print "Test {}".format(i)
    for row in d[::-1]:
        print row[::-1]
