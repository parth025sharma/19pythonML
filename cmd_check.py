#!/usr/bin/python3
import os
cmd=input("Enter word to find if it is a command or not:-")
#returned_value = os.system("echo $?")
if os.system("echo $?")==0:
        print(cmd + "is a command")
        os.system(cmd)
else :
        print("It is not a comand")
