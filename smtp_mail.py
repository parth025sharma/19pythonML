#!/usr/bin/python3

#
import smtplib#importing smtp liberary

import ssl#importing ssl for secured socket layer 

import getpass#to hide password taken as input

port=465 #port used under ssl

smtp_server="smtp.gmail.com"

#email-id of sender with password conformation 

sender=input("sender'semail::")
passwd=input("enter your password")

#receiver email
recv=input("send to::")

#message to send

message= input("enter message to send::")
#to enable hostname checking
con=ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server,port,context=con) as server:
	server.login(sender,passwd)
	server.sendmail(sender,recv,message)



