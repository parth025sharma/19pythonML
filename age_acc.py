#!/usr/bin/python3
import os
from datetime import datetime
yr=datetime.today().year
age=int(input("Enter your age: "))
name=input("Enter your name: ")
if  age>95:
        age=age-95
        yr=yr-2
        print("year in ehich you were 95 was: ",yr)
else:
        age=95-age
        yr+=age
        print("year in which you will turn 95 is: ",yr)
