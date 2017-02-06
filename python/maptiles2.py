import sys

quadkey_s=sys.stdin.readline().strip()
quadkey=int(quadkey_s)

zoom=len(quadkey_s)

x=int("".join([bin(int(i))[-1].replace('b','0') for i in list(quadkey_s)]),2)
y=int("".join([bin(int(i))[-2].replace('b','0') for i in list(quadkey_s)]),2)

print zoom, x, y

