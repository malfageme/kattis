import sys

i=0
winner=[0,0]
for line in sys.stdin:
    i+=1
    score=sum(map(int,line.split()))
    if score>winner[1]:
        winner[1]=score
        winner[0]=i

print " ".join(map(str,winner))
