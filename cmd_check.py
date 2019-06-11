#!/usr/bin/python3
import os,sys
import subprocess as sp
f=open("command.txt","a")
y='Y'
while y=='Y':
        cmd=input("Enter word to find if it is a command or not:-")
        p=sp.getoutput( cmd+ " >/dev/null ; echo $?")
        c=cmd
        if p=='0':
                    print(cmd + " is a command")
                    os.system(cmd)
                    f.write(cmd+" \n")


        else:
                     print(cmd +" It is not a command") 
                     f.write(cmd+"\n")
        y=input("If you want to enter more press Y(capital):")
        cmd=input("Enter word to find if it is a command or not:-")
        if c==cmd:
                os.system("echo not to do this again | festival --tts")
                sys.exit()
        else:
                continue


f.close()
