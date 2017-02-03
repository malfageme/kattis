import sys

pattern="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

for line in sys.stdin:
    if line.split()[0]=="0":
        break
    n,pt=line.split()
    n=int(n)

    print "".join([pattern[(pattern.index(c)+n)%len(pattern)] for c in pt[::-1]])

