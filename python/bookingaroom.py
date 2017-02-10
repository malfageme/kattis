import sys

r,n=map(int,sys.stdin.readline().split())

booked=[]
for _ in range(n):
    booked.append(int(sys.stdin.readline()))

for i in range(1,r+1):
    if i not in booked:
        print i
        break
else:
    print 'too late'
