import sys

num_cases=int(sys.stdin.readline())
c="Simon says "

for _ in range(num_cases):
    line=sys.stdin.readline().strip()
    i=line.find(c)
    if i==0 and len(line)>len(c):
        print line[len(c):]

