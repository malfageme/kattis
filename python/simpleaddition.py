import sys

sys.setrecursionlimit(200000)

a=sys.stdin.readline().strip()
b=sys.stdin.readline().strip()

def my_add(a,b,remain=0):
    result=[]
    if len(a)==0:
        if len(b)==0:
            return "" if remain==0 else str(remain)
        else:
            new_digit=int(b[-1])+remain
            return my_add(a,b[:-1],new_digit/10)+str(new_digit%10)
    elif len(b)==0:
            new_digit=int(a[-1])+remain
            return my_add(a[:-1],b,new_digit/10)+str(new_digit%10)
    else:
            new_digit=int(a[-1])+int(b[-1])+remain
            return my_add(a[:-1],b[:-1],new_digit/10)+str(new_digit%10)

print my_add(a,b)

