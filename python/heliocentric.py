import sys

case=0
for line in sys.stdin:
    case+=1
    e,m=map(int,line.split())
    step=687-m
    i=0
    while (e%365)!=0 or (m%687)!=0:
        if i==0:
          e+=step
          m+=step
        else:
          m+=687
          e+=687
        i+=1
    print 'Case {}: {}'.format(case,max(i-1,0)*687+min(i,1)*step)

