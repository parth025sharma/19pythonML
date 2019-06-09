#!/usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
range5=[]
range2=[]
for i in adhoc:
        if i>5:
                range5.append(i)
        elif i<=2:
                range2.append(i)
print("Number greater then 5: ",range5)
print("Number smaller then or equal to 2: ",range2)
