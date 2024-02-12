# Good luck!
n = int(input()) # amount of days
List =list(map(int, input().split())) #n space-seperated integers; price of stock over n days

max=0
min=List[0]

for i in range(n):
    profit = List[i] - min
    if profit < 0:
        min=List[i]
    elif  profit > max:
        max=profit
print(max)