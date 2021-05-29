import csv

f = open('Internet Users.csv',newline='')

rf = csv.reader(f)

filelist= list(rf)
filelist.pop(0)

l = len(filelist)

lst = []

median = 0

for i in range(l):
    lst.append(float(filelist[i][1]))

lst.sort()

if(l%2==1):
    median = lst[l//2]

elif(l%2==0):
    eve = lst[l//2]
    odd = lst[l//2-1]
    val = (eve+odd)/2
    median = val
    print(6/2)

print(median)