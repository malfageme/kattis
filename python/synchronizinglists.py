import sys


while True:
    n=int(sys.stdin.readline())    
    if n==0:
        break

    l1=[]
    for _ in range(n):
        l1.append(int(sys.stdin.readline()))
    l1_s=sorted(l1,reverse=False)
    l1_keys=[l1_s.index(x) for x in l1]

    l2=[]
    for i in range(n):
        l2.append(int(sys.stdin.readline()))

    l2_s=sorted(l2)
    l2_right=[l2_s[x] for x in l1_keys]

    for num in l2_right:
        print num
    print

