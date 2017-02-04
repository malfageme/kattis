import sys

num_datasets=int(sys.stdin.readline())

for line in sys.stdin:
    k,n=map(int,line.split())

    print k, sum(range(n+1)), sum(range(1,(2*n)+1,2)), sum(range(0,(2*n)+1,2))


