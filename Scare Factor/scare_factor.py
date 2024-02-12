# ---------------------------------------------------
# Name : Ayra Qutub
# SID: 1708104
# CCID : aqutub
# AnonID : 1000316555
# CMPUT 274 , Fall 2022
#
# Morning Problem: Scare Factor
# ---------------------------------------------------


n, m, k = map(int, input().split())
# n = number of auditoriums
# m = amount of movies
# k = maximum cumulative scare factor
List=[]
for i in range(n):
    ns=list(map(int, input().split(' ')))
    List.append(ns)
# print(List)

transposed = list()
for i in range(len(List[0])):
    row = list()
    for sublist in List:
        row.append(sublist[i])
    transposed.append(row)

minList=[]
for line in transposed:
    m=min(line)
    minList.append(m)
# print(minList)
minList.sort()

scarFac = 0
numMov = 0

for i in minList:
        scarFac += i
        if scarFac <= k:
            numMov += 1
        elif scarFac > k:
            scarFac -= 1
print(numMov)