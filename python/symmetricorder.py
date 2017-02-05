import sys

case=0
while 1:
    case+=1
    num_lines=int(sys.stdin.readline())
    if num_lines==0:
        break
    print "SET {}".format(case)
    names_list=[]
    for _ in range(num_lines):
        names_list.append(sys.stdin.readline().strip())
    l=len(names_list)
    for name in names_list[:l:2]:
        print name
    if l>1:
        for name in names_list[l-1-(l%2)::-2]:
            print name

