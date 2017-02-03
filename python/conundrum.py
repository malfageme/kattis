import sys

line=sys.stdin.readline().strip().lower()
pattern="per"

print len([c for i in range(len(pattern)) for c in line[i::len(pattern)] if c!=pattern[i]])


