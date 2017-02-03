import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    l=map(int,sys.stdin.readline().split())
    non_born=0
    for i in range(1,len(l)):
        new_turtles=l[i]-2*l[i-1]
        if new_turtles>0:
            non_born+=new_turtles
    print non_born

