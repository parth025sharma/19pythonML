#!/usr/bin/python3
from datetime import datetime
tme=datetime.now()
x=tme.hour
name=str(input("Can I get your name: "))
if x>=5 and x<12 :
        print("Good morning "+str(name))
elif x>12 and x>=17 and x>0: 
        print("good afternoon "+str(name))
elif x==12:
        print("good noon "+str(name))
elif x>17 and x<=22:
        print("Good evening "+str(name))
else:
        print("Good night "+str(name))
        
