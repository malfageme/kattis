import sys

line=sys.stdin.readline().strip()

vowels="aeiou"
i=0
msg=""
while i<len(line):
    msg+=line[i]
    i+=1 if line[i] not in vowels else 3

print msg
