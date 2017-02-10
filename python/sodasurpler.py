import sys

e,f,c=map(int,sys.stdin.readline().split())

empty_remaining=e+f

drunk_sodas=0
while empty_remaining>=c:
    new_sodas=empty_remaining/c
    empty_remaining%=c
    drunk_sodas+=new_sodas
    empty_remaining+=new_sodas

print drunk_sodas
