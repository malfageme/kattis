import sys

num=int(sys.stdin.readline())
print int("{:b}".format(num)[::-1],2)
