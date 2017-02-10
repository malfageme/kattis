import sys

for line in sys.stdin:
    sweet,sour=map(int,line.split())
    if sweet==sour==0:
        break

    if sweet+sour==13:
        print 'Never speak again.'
    elif sweet>sour:
        print 'To the convention.'
    elif sour>sweet:
        print 'Left beehind.'
    else:
        print 'Undecided.'


