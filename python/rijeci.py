import sys

def f(a,b):
    return b, a+b

num_pressed=int(sys.stdin.readline())

a=1
b=0
for _ in range(num_pressed):
    a,b=f(a,b)

print a,b
