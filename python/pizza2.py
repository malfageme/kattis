import sys

r,c=map(int,sys.stdin.readline().split())

in_surface=((r-c)**2)
pizza_surface=(r**2)

if pizza_surface>0:
    print (float(in_surface)/pizza_surface)*100
else:
    print 0
