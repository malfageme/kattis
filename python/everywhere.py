import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    trips=int(sys.stdin.readline())
    cities={}
    for _ in range(trips):
        cities[sys.stdin.readline().strip()]=True
    print len(cities.keys())
