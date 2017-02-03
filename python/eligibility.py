import sys

num_cases=int(sys.stdin.readline())

for line in sys.stdin:
    name,start_date,birth_date,courses=line.split()
    courses=int(courses)
    start_year=int(start_date.split("/")[0])
    birth_year=int(birth_date.split("/")[0])

    if start_year>=2010 or birth_year>=1991:
        print name, "eligible"
    elif courses/5.0 > 8:
        print name, "ineligible"
    else:
        print name, "coach petitions"

