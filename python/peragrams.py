import sys

letters={}
word=sys.stdin.readline().strip()

for c in word:
    try:
        letters[c]+=1
    except:
        letters[c]=1

odd_letters=len([x for x in letters.values() if x%2==1])

print max(odd_letters-1,0)
