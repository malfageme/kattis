#!/usr/bin/python
""" Cokolada problem """
import sys

k = int(sys.stdin.readline())

def find_min(k, odd=0):
    if k==1 or k==0:
        return 1 + (1 if odd>0 else 0)
    else:
        return 2 * find_min(k/2,odd+k%2)

n = find_min(k)
k_s = bin(k)
n_s = bin(n)

print n, k_s[2:].rfind('1')+len(n_s)-len(k_s)

