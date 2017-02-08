import sys

n=int(sys.stdin.readline())

status=None
old_name=None
for line in sys.stdin:
    if not status and old_name:
        status='INCREASING' if line>old_name else 'DECREASING'
    elif (status=='INCREASING' and old_name>line) or (status=='DECREASING' and old_name<line):
            print 'NEITHER'
            break
    old_name=line
else:
    print status
        
