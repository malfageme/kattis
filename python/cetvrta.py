import sys
from itertools import product

points=[]
min_x, min_y, max_x, max_y=1000, 1000, 0, 0

for line in sys.stdin:
    x,y=map(int,line.split())
    points.append((x,y))
    min_x=min(min_x,x)
    min_y=min(min_y,y)
    max_x=max(max_x,x)
    max_y=max(max_y,y)

for point in product((min_x,max_x),(min_y,max_y)):
    if point not in points:
        print " ".join(map(str,(point)))

