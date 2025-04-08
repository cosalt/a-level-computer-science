import random

arraydata = [[random.randint(1,100) for i in range(10)] for i in range(10)]

arraylength = 10

for x in range(0, arraylength-1):
    for y in range(0, arraylength-2):
        for z in range(0, arraylength - y - 2):
            if arraydata[x][z] > arraydata[x][z+1]:
                tempvalue = arraydata[x][z]
                arraydata[x][z] = arraydata[x][z+1]
                arraydata[x][z+1] = tempvalue


for j in arraydata:
    print(j)
