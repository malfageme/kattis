import sys

a,b,c,d=map(int,sys.stdin.readline().split())
#p,m,g=map(int,sys.stdin.readline().split())
times_heroes=map(int,sys.stdin.readline().split())

for t in times_heroes:
    dog1=((t/(a+b))*(a+b)<t) and ((t/(a+b))*(a+b)+a>=t)
    dog2=((t/(c+d))*(c+d)<t) and ((t/(c+d))*(c+d)+c>=t)
    if dog1 and dog2:
        print "both"
    elif dog1 or dog2:
        print "one"
    else:
        print "none"
