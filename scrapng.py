#!/usr/bin/python3
import time
from googlesearch import search
web =input("Enter anything to search: ")
url=[]
for i in search(web,stop=10):
        print(i)
        time.sleep(2)
        url.append(i)
print(url)
with open('list.txt', 'w') as filehandle:  
    for itm in url:
        filehandle.write('%s\n' % itm)

