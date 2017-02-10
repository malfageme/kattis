import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    stops=int(sys.stdin.readline())
    people=0
    for stop in range(stops):
        people=people*2+1
    print people
