import sys

n=sorted(map(int, sys.stdin.readline().split()))

def cal_sol(n,d,i):
    if i==len(n)-1:
        return n[i]+d if n[i]+d<=100 else n[0]-d
    return n[i]+d if n[i+1]-n[i]>d else cal_sol(n,d,i+1)
    
d=min(n[1]-n[0],n[2]-n[1])
print cal_sol(n,d,0)

