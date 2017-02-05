import sys
from math import pi, sqrt


for line in sys.stdin:
    d,v=map(int,line.split())
    if d==v==0:
        break
    #max_v=pi/4*d**3
    #print max_v
    #cones_area=(pi/3)*(d/2)*(d/2)*(d/2)*2
    #v_without_cones=pi/6*d**3
    #v_remain=pi/6*d1**3
    #v_taken=v_without-v_remain
    # v_remain=v_without_cones - v
    # (pi*d1*d1*d1)/6 = (pi*d**3)/6 - v
    d1 = ((d**3)-(6*v/pi))**(1.0/3)
    print d1
    

