#!/usr/bin/python3
row=int(input("enter row dimenshion:"))
column=int(input("enter column dimenshion:"))
array=np.random.random((row,column))
np.savetxt("file.txt", array)

