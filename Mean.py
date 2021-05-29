import csv

f = open('Interenet Users.csv',newline='')

rf = csv.reader(f)

fileList = list(rf)
fileList.pop(0)

l = len(fileList)

add = 0

for i in range(l):
    Users=float(fileList[i][1])
    add += Users

mean = add/l

print(mean)
