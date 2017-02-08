import sys
from math import acos, pi

for line in sys.stdin:
    r,x,y=map(float,line.split())
    d=(x**2 + y**2)**(1.0/2)
    if d>=r:
        print "miss"
    else:
        angle=acos(d/r)
        area_section=acos(d/r)*(r**2)

        area_triangle=d*((r**2 - d**2)**(1.0/2))
        area_chord=area_section-area_triangle
        print pi*r**2-area_chord, area_chord
