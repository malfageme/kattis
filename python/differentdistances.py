import sys

for line in sys.stdin:
    if line.strip()=="0":
        break
    x1,y1,x2,y2,p=map(float,line.split())
    print ( abs(x1-x2)**p + abs(y1-y2)**p ) ** (1.0/p)
