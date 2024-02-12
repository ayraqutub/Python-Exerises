# Good luck on this morning problem!
l, c, n, t = map(int, input().split())
# l = length of road trip
# c = capacity of gas tank
# n = number of gas stations
# t = amount of time it takes to refuel

input = list(map(int, input().split()))
locations=[0]
locations += input
locations.append(l)
stops = 0
gasTank = c

for i in range(1,n+1):
    dist = locations[i] - locations[i-1]
    dist2 = locations[i+1]-locations[i]
    gasTank -= dist
    if gasTank - dist2 < 0:
        stops += 1
        gasTank = c
    
    
"""
if locations[0] == c:
    stops += 1
for i in range(0, n-2):
    if locations[i+1]-locations[i] >= c: 
        stops += 1
    elif locations[i+2]-locations[i] >= c:
        stops += 1
if l-locations[n-1] >= c:
    stops += 1
"""


totTime = l + t*int(stops)

print(totTime)