import sys
from collections import Counter

case=0
while True:
    case+=1
    num_animals=int(sys.stdin.readline())
    if num_animals==0:
        break
    c=Counter()
    for _ in range(num_animals):
        animal=sys.stdin.readline().strip()
        type_animal=animal.split()[-1].lower()
        c[type_animal]+=1

    print 'List {}:'.format(case)
    for animal in sorted(c.keys()):
        print "{} | {}".format(animal,c[animal])
