import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    l1=sys.stdin.readline().strip()
    l2=sys.stdin.readline().strip()
    res=["." if x[0]==x[1] else "*" for x in zip(l1,l2)]
   
    print l1 
    print l2 
    print "".join(res)

