import sys

num_cases=int(sys.stdin.readline())

for _ in range(num_cases):
    students=map(int,sys.stdin.readline().split())
    case=students[0]
    students=students[1:]
    students_sort=[]
    steps=0
    for student in students:
        if len(students_sort)==0:
            students_sort.append(student)
        else:
            for i in range(len(students_sort)):
                if students_sort[i]>student:
                    steps+=len(students_sort[i:])
                    students_sort=students_sort[:i]+[student]+students_sort[i:]
                    break
            else:
                students_sort.append(student)
    print case, steps

