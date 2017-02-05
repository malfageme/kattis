import sys

line=sys.stdin.readline().strip()

c={'P':[], 'K':[], 'H':[], 'T':[]}

i=0
while i < len(line):
    suit=line[i]
    card=int(line[i+1:i+3])
    if card in c[suit]:
        print 'GRESKA'
        exit(0)
    c[suit].append(card)
    i+=3

print 13-len(c['P']), 13-len(c['K']), 13-len(c['H']), 13-len(c['T'])
