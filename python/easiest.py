import sys

def sum_digits(num):
    return sum(map(int,str(num)))

for line in sys.stdin:
    num=int(line)
    if num==0:
        break
    target=sum_digits(num)
    test=11
    while sum_digits(test*num)!=target:
        test+=1
    print test

