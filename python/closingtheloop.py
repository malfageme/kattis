import sys
from operator import add

num_cases=int(sys.stdin.readline())

for case in range(num_cases):
    num_segments=int(sys.stdin.readline())
    segments_read=sys.stdin.readline().split()
    segments={'R':[],'B':[]}


    for s in segments_read:
        segments[s[-1]].append(int(s[:-1]))

    segments_used=min(map(len,segments.values()))
    total=0
    if segments_used>0:
        for s in segments.values():
             total+=sum(sorted(s)[-segments_used:])-segments_used
    print "Case #{}: {}".format(case+1,total)
