#!/usr/bin/python3
import os,sys
import subprocess as sp
f=open("command.txt","a+")
cmd=input("Enter word to find if it is a command or not:-")
y='Y'
f.seek(0)
while f.read() is 0:
                if cmd not in f.read():
                        
                    p=sp.getoutput( cmd+ " >/dev/null ; echo $?")
                    if p=='0':
                            print(cmd + " is a command")
                            os.system(cmd)
                            f.write(cmd+" \n")


                    else:
                        print(cmd +" It is not a command") 
                        f.write(cmd+"\n")
                    y=input("If you want to enter more press Y(capital):")
                    cmd=input("Enter word to find if it is a command or not: ")
                    f.seek(0)
                else:

                    os.system("echo not to do this again | festival --tts")
                    sys.exit()
f.close()
