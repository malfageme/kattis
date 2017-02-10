import sys

num_cases=int(sys.stdin.readline())
set_complete=set('abcdefghijklmnopqrstuvwxyz')
for case in range(num_cases):
    set_read=set(sys.stdin.readline().strip().lower())
    missing=set.difference(set_complete, set_read)
    print 'pangram' if len(missing)==0 else 'missing {}'.format(''.join(sorted(missing)))
