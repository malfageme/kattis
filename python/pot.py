import sys

num_cases=int(sys.stdin.readline())

total=0
for _ in range(num_cases):
    line=sys.stdin.readline().strip()
    total+=int(line[:-1])**int(line[-1:])

print total
