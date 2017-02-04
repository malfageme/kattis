import sys

num_cases=int(sys.stdin.readline())

for case in range(1,num_cases+1):
    g=int(sys.stdin.readline())
    c_list=map(int,sys.stdin.readline().split())
    guests={}
    for guest in c_list:
        try:
            guests[guest]+=1
        except:
            guests[guest]=1
    print "Case #{}:".format(case), [x[0] for x in guests.items() if x[1]==1][0]

