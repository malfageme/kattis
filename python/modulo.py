import sys

numbers={}
for line in sys.stdin:
    num=int(line)
    numbers[num%42]=True

print len(numbers.keys())
