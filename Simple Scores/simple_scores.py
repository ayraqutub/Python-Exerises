# ---------------------------------------------------
# Name : Ayra Qutub
# SID: 1708104
# CCID : aqutub
# AnonID : 1000316555
# CMPUT 274 , Fall 2022
#
# Morning Problem : simple_scores
# ---------------------------------------------------

n=int(input())
accidentals=input()
sharp = accidentals.count('#')
flat = accidentals.count('b')

num = sharp-flat

if num<0:
    print('b'*abs(num))
elif num>0:
    print('#'*num)
else:
    print('0')  
