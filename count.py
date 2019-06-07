#!/usr/bin/python
#taking input of string
countdigit=0
countalpha=0
countspace=0 
string = input("Enter string:")
for i in range(0,len(string)):
    if string[i].isdigit()==1:
        countdigit +=1
    elif string[i].isalnum()==1:
        countalpha +=1
    elif string[i]==' ':
        countspace +=1    
    else :
    	print(string)
print("NUMBER OF DIGITS:" , countdigit)
print("NUMBER OF ALPHABETS:" , countalpha)
print("NUMBER OF SPACES:" , countspace)


