import sys

for line in sys.stdin:
    month,day,year,sunrise,sunset=line.split()
    day=int(day)
    year=int(year)
    sunrise_h,sunrise_m=map(int,sunrise.split(':'))
    sunset_h,sunset_m=map(int,sunset.split(':'))

    min_sun=(sunset_h*60+sunset_m)-(sunrise_h*60+sunrise_m)
    print "{} {} {} {} hours {} minutes".format(month, day, year, min_sun/60, min_sun%60)

