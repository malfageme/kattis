import sys

num_samples=int(sys.stdin.readline())

while num_samples>0:
    time_total=0
    miles_total=0
    for _ in range(num_samples):
        speed, time=map(int, sys.stdin.readline().split())
        miles_total+=(time-time_total)*speed
        time_total=time
    print "{} miles".format(miles_total)
    num_samples=int(sys.stdin.readline())

