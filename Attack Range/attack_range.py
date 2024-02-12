# ---------------------------------------------------
# Name : Ayra Qutub
# SID: 1708104
# CCID : aqutub
# AnonID : 1000316555
# CMPUT 274 , Fall 2022
#
# Morning Problem: Attack Range
# ---------------------------------------------------

n, m = map(int, input().split())
enemy_range = list(map(int, input().split())) # list(map(...))
class_range = list(map(int, input().split()))
#enemy_list= enemy_range.split()
#class_list= class_range.split()
new_list=[]
errorMess = -1
for elem in class_range:
    if elem >max(enemy_range):
        new_list.append(elem)
if new_list == []:
    print(errorMess)
else:
    print(min(new_list))