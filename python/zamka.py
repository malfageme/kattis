import sys

l=int(sys.stdin.readline())
d=int(sys.stdin.readline())
x=int(sys.stdin.readline())

n,m=100000,0
for i in range(l,d+1):
    if sum(map(int,str(i)))==x:
        n=i
        m=i
        break

for i in range(d,n,-1):
    if sum(map(int,str(i)))==x:
        m=i
        break

print n
print m

