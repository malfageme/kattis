import sys

num_cases=int(sys.stdin.readline())

for case in range(num_cases):
    d,m=map(int, sys.stdin.readline().split())
    days_month=map(int, sys.stdin.readline().split())
    # Sunday == 0 => Friday == 5
    current_day_year=1
    current_day_month=1
    current_day_week=0
    current_month=0
    fridays=0
    while current_day_year < d:
        if current_day_year%7==6:
            fridays+=1
        #current_day_month=1
        offset=0
        # Advance to the first day of the next month
        if current_day_month!=1:
            offset=days_month[current_month]-current_day_month+1
            current_month+=1
            current_day_month=1
        if current_month>m:
            break
        while current_day_month!=13:
            if current_month>=m:
                break
            if days_month[current_month]<13:
                offset+=days_month[current_month]
                current_month+=1 
                current_day_month=1
            else:
                offset+=12
                current_day_month=13
        current_day_year+=offset
    print fridays
            
        
