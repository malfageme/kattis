import sys

a,b,c=map(int,sys.stdin.readline().split())

if a+b==c:
    print "{}+{}={}".format(a,b,c)
elif a==b+c:
    print "{}={}+{}".format(a,b,c)
elif a-b==c:
    print "{}-{}={}".format(a,b,c)
elif a==b-c:
    print "{}={}-{}".format(a,b,c)
elif a*b==c:
    print "{}*{}={}".format(a,b,c)
elif a==b*c:
    print "{}={}*{}".format(a,b,c)
elif b!=0 and (1.0*a)/b==c:
    print "{}/{}={}".format(a,b,c)
elif c!=0 and a==(1.0*b)/c:
    print "{}={}/{}".format(a,b,c)


