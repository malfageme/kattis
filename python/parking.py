import sys

cost_table=[0]+map(int,sys.stdin.readline().split())

def next_event(time,trucks):
     arrival=min([(x[0] if x[0]>time else 999999) for x in trucks])
     departure=min([(x[1] if x[1]>time else 999999) for x in trucks])
     t_event=min(arrival,departure)
     arrivals=[1 for x in trucks if x[0]==t_event]
     departures=[-1 for x in trucks if x[1]==t_event]
     return t_event,arrivals+departures
     

trucks=[]
for line in sys.stdin:
    trucks.append(map(int,line.split()))

t=0
trucks_parked=0
total_cost=0
while t<999999:
    next_t,events=next_event(t, trucks)
    total_cost+=cost_table[trucks_parked]*(next_t-t)*trucks_parked
    trucks_parked+=sum(events)
    t=next_t

print total_cost
