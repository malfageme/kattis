import sys

max_line=0
text=[]
for line in sys.stdin:
    line=line.strip()
    max_line=max(max_line, len(line))
    text.append(len(line))


print sum([(max_line-x)**2 for x in text[:-1]])
