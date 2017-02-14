import sys

p,s=sys.stdin.readline().split()

index_p=0
index_s=0

while index_s<len(s):
    if s[index_s]==p[index_p]:
        index_p+=1
        if index_p==len(p):
            break
    elif s[index_s] in p[index_p:]:
        break
    index_s+=1

if index_p==len(p):
    print 'PASS'    
else:
    print 'FAIL'
