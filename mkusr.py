#!/usr/bin/python3
import os
import sys
nme=input("Enter name by which you want to make user: ")
for i in nme:
        if i.isalpha()==1:
                continue
        else:
                print("There is a non character element exiting....")
                sys.exit()
pswd="hello"+nme
os.system("sudo useradd -p "+pswd+" "+nme)
print("User added successfully")
