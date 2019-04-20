#############################################
##   PRESENCE AUTOMATION - MAIL SHUTDOWN   ##
##       MADE BY : ABHISHEK IYENGAR        ## 
##          YT : ANNOYING ERRORS           ##
##           GITHUB : tinshade             ##
#############################################

       ##AUTOMATE LIFE WITH PYTHON##

#For Checking Internet Connection
import urllib3
import win32api
import time
import sys

#For Checking Email
import email
import imaplib
import mailbox

#Verify Email Authentication
import re

#Interact With OS
import os
import os.path
from os import path
from _winreg import *
import uuid

#For scheduling task execution
import schedule

#TO START ON BOOT.
def addStartup():  
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'PresenceAutoShut', 0, REG_SZ,new_file_path)

if path.exists('Pref.xml'):
	#Pref.xml will contain all the user preferences like emailID to be used, password and custom check time
	#(TO BE IMPLEMENTED WITH UI VERSION)
    pass
else:
    addStartup() #Calling the AddStartup function
    print("Added to STARTUP")

#CHECKING FOR INTERNET CONNECTION
def connected():
	http = urllib3.PoolManager()
	try :
		urllib3.disable_warnings() #Disables warning caused by untrusted HTTP request
		url = http.request('GET', 'https://www.youtube.com/channel/UCoKvMf0XfGYSuujgL6dFSeA') #Link to my YT Channel, please subscribe :P
		if url.status == 200:
			pass

	except urllib3.exceptions.MaxRetryError as e:
		#print(e) #Debugging
		win32api.MessageBox(0, 'You are not connected to the Internet. \nRestart when connected!', 'Inactive', 0x00001000) #Display non-maskable interrupt
		sys.exit(0) #Quits the program

connected() #Call everytime the program is started after boot
EMAIL_ACCOUNT = "mailID" #User's email (Mails will be checked for this ID)
PASSWORD = "password" #User's Password
#LOGIN AND GATHER ALL MAILS
mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
#MAIN FUNCTION
def shutter():
	mail.select('INBOX')
	result, data = mail.uid('search',None, '(SUBJECT "Shutdown")', 'UNSEEN')
	i = len(data[0].split())
	#ITERATE THROUGH MAILS
	for x in range(i):
	    latest_email_uid = data[0].split()[x]
	    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	    raw_email = email_data[0][1]
	    raw_email_string = raw_email.decode('utf-8')
	    email_message = email.message_from_string(raw_email_string)
	    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))	#Fetch the sender IDs
	    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))	#Fetch mail subjects
	    print(subject)
	    #Format the ID
	    lst = re.findall(EMAIL_ACCOUNT, email_from)
	    p = str(lst)
	    r1 = p.replace(r"[","")
	    r2 = r1.replace(r"]","")
	    r3 = r2.replace(r"'","")
	    #VALIDATING SENDER
	    if r3 == EMAIL_ACCOUNT:
	        if subject == "Shutdown":
	            if r3 == EMAIL_ACCOUNT:
	                #print(r3) #Debugging
	                #DELETE THE MAIL IF FOUND TO REMOVE CLUTTER
	                try:
	                    typ, data = mail.search(None, 'subject',subject, 'from',EMAIL_ACCOUNT)
	                    for num in data[0].split():
	                        mail.store(num, '+FLAGS', '\\Deleted') #Mark for deletion
	                        mail.expunge() #Delete everything marked
	                        mail.close()
	                        sentclutter() #Run the clutter remover function
	                        mail.logout() #Logout
	                        #print("Would've shutdown") #Debugging
	                        os.system('shutdown /p /f')	#Shutdown Windows immediately, without warning
	                #IndexError appears the first time only.
	                except IndexError:
	                    print("ok")
	                    continue
	            else:
	            	typ, data = mail.search(None, 'subject',subject, 'from',EMAIL_ACCOUNT)
	                for num in data[0].split():
	                    mail.store(num, '-FLAGS', '\\SEEN') #Mark for deletion
	                    mail.expunge() #Delete everything marked
	                    mail.close()
	        else:
	        	typ, data = mail.search(None, 'subject',subject, 'from',EMAIL_ACCOUNT)
	        	for num in data[0].split():
	        		mail.store(num, '-FLAGS', '\\SEEN') #Mark for deletion
	        		mail.expunge() #Delete everything marked
	        		mail.close()
	    else:
	    	typ, data = mail.search(None, 'subject',subject, 'from',EMAIL_ACCOUNT)
	    	for num in data[0].split():
	    		mail.store(num, '-FLAGS', '\\SEEN') #Mark for deletion
	    		mail.expunge() #Delete everything marked
	    		mail.close()

def sentclutter():
	mail.select('[Gmail]/Sent Mail')
	result, data = mail.uid('search',None, '(SUBJECT "Shutdown")', 'ALL')
	i = len(data[0].split())
	#ITERATE THROUGH MAILS
	for x in range(i):
	    latest_email_uid = data[0].split()[x]
	    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	    raw_email = email_data[0][1]
	    raw_email_string = raw_email.decode('utf-8')
	    email_message = email.message_from_string(raw_email_string)
	    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))	#Fetch the sender IDs
	    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))	#Fetch mail subjects
	    print(subject)
	    #Format the ID
	    lst = re.findall(EMAIL_ACCOUNT, email_from)
	    p = str(lst)
	    r1 = p.replace(r"[","")
	    r2 = r1.replace(r"]","")
	    r3 = r2.replace(r"'","")
	    #VALIDATING SENDER
	    if r3 == EMAIL_ACCOUNT:
	        if subject == "Shutdown":
	            if r3 == EMAIL_ACCOUNT:
	                #print(r3) #Debugging
	                #DELETE THE MAIL IF FOUND TO REMOVE CLUTTER
	                try:
	                    typ, data = mail.search(None, 'subject',subject, 'from',EMAIL_ACCOUNT)
	                    for num in data[0].split():
	                        mail.store(num, '+FLAGS', '\\Deleted') #Mark for deletion
	                        mail.expunge() #Delete everything marked
	                        mail.close() 
	                        print("Clutter Removed") #Debugging
	                except IndexError:
	                    continue
shutter()
#EVENT SCHEDULER
def scheduler():
	schedule.every(10).seconds.do(connected) #Check for connection every 10 seconds
	schedule.every(10).seconds.do(shutter) #Run the mail function every 10 seconds
	while True:
	    schedule.run_pending()
scheduler()
