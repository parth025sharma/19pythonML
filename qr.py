#!/usr/bin/python3
import pyqrcode
from googlesearch import search
web =input("Enter anything to search: ")
j=0
for i in search(web,tld="co.in",stop=3):
        j=j+1
        url=pyqrcode.create(i)
        url.svg("qrscan.svg"+str(j),scale=8)
