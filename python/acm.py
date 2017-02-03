import sys

solved={}
tries={}

for line in sys.stdin:
    if line[0]=="-":
        break
    time,problem,result=line.split()
    time=int(time)
    if problem not in solved.keys():
        try:
            tries[problem]+=1
        except:
            tries[problem]=1
        if result=="right":
            solved[problem]=time

print len(solved), sum((tries[p]-1)*20+solved[p] for p in solved.keys())
