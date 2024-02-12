# ---------------------------------------------------
# Name : Ayra Qutub
# SID: 1708104
# CCID : aqutub
# AnonID : 1000316555
# CMPUT 274 , Fall 2022
#
# Morning Problem: N-Sum
# ---------------------------------------------------

n, m = map(int, input().split())
#initialize empty lists
l=[]
backw_k=[] 

for i in range(n, 0, -1): #fill l with numbers from 1 to n, in reverse order
    l.append(i)

sum = 0 #initialize
for i in l:  #create list in backwards numerical order to ensure highest value numbers
    sum += i
    if sum <= m:
        backw_k.append(i)
    else:
        sum -=i

k=[] #initialize
for i in range(len(backw_k)-1, -1, -1): #fix list to be in ascending order
    k.append(backw_k[i])

print(len(k))
print(' '.join((list(map(str, k)))))
