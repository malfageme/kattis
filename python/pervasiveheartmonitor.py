import sys

for line in sys.stdin:
    tokens=line.split()
    rates=[]
    name=''
    for rate in tokens:
        try:
            rates.append(float(rate))
        except:
            name+=' '+rate
    print "{:.3f} {}".format(sum(rates)/len(rates), name[1:])
