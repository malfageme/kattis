import sys

gunnar=map(int,sys.stdin.readline().split())
emma=map(int,sys.stdin.readline().split())
gunnar_ave=sum(gunnar)*1.0/len(gunnar)
emma_ave=sum(emma)*1.0/len(emma)

if gunnar_ave>emma_ave:
    print "Gunnar"
elif emma_ave>gunnar_ave:
    print "Emma"
else:
    print "Tie"

