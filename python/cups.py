import sys

num_cups=int(sys.stdin.readline())
cups={}

for line in sys.stdin:
    line=line.split()
    radius=0
    color=""
    try:
        radius=int(line[0])/2.0
        color=line[1]
    except:
        color=line[0]
        radius=int(line[1])
    cups[radius]=color
   
for cup in sorted(cups.items()):
    print cup[1]
 
