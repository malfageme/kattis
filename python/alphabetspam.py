import sys

line=sys.stdin.readline().strip()

def find_group(c):
    if c=="_":
       return 0
    if c>='a' and c<='z':
       return 1
    if c>='A' and c<='Z':
       return 2
    return 3


total={0:0,1:0,2:0,3:0}

for c in line:
    group=find_group(c)
    total[group]+=1

for i in range(4):
    try:
        print float(total[i])/len(line)
    except:
        print 0

