import sys

r,c=map(int, sys.stdin.readline().split())

def extract_min(d):
    min_word=chr(255)*21
    for row in d:
        for word in row.split("#"):
            if len(word)>=2 and word < min_word:
                    min_word=word
    return min_word

d=[]
min_word=chr(255)*21
for line in sys.stdin:
    d.append(line.strip())

min_word=extract_min(d)
new_min_word=extract_min(["".join(row) for row in zip(*d)])
print new_min_word if new_min_word<min_word else min_word

