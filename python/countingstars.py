import sys

sys.setrecursionlimit(20000)

def check_counted(grid, counted, i, j):
    m=len(grid)
    n=len(grid[i])
    if grid[i][j]=='-' and not counted[i][j]:
        counted[i][j]=True
        if i>0:
            check_counted(grid,counted,i-1,j)
        if j>0:
            check_counted(grid,counted,i,j-1)
        if i<m-1:
            check_counted(grid,counted,i+1,j)
        if j<n-1:
            check_counted(grid,counted,i,j+1)



case=0
while True:
    line=sys.stdin.readline()
    if not line:
        break
    case+=1
    m,n=map(int,line.split())

    grid=[]
    counted=[]
    for _ in range(m):
        grid.append(sys.stdin.readline().strip())
        counted.append([False]*(2*len(grid[-1])))

    num_stars=0
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='-':
                if not counted[i][j]:
                    check_counted(grid, counted, i, j)
                    num_stars+=1

    print 'Case {}: {}'.format(case,num_stars)

