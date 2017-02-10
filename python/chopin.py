import sys
from operator import add

mult_names=(('A#','Bb'), ('C#','Db'), ('D#','Eb'), ('F#','Gb'), ('G#','Ab'))

case=0
for line in sys.stdin:
    case+=1
    note,tonality=line.split()
    try:
        print 'Case {}: {} {}'.format(case,[set.difference(set((x,y)),set([note])) for x,y in mult_names if note==x or note==y][0].pop(),tonality)
    except:
        print 'Case {}: UNIQUE'.format(case)


