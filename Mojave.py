"""
	THE MOJAVE WALLPAPER EFFECT

	Setting dynamic time-based wallpapers like in 
	Mac OS's Mojave update

	
"""
import ctypes #To change the wallpaper
from datetime import datetime #To know what time it is
import os #To enable the start-on-boot functionality
import win10toast #To enable toasts for Windows for notification
import time #To schedule events


#To add the script to start-up
import sys 
import winreg as reg
 



#Image paths
#Absolute path is like "E:\Images\image.jpg"

<<<<<<< HEAD
Morning = r"<Absolute_Path>1.jpeg" #Morning image
Afternoon = r"<Absolute_Path>2.jpeg" #Afternoon image
Evening = r"<Absolute_Path>3.jpeg" #Evening image
Night = r"<Absolute_Path>4.jpeg" #Night image
=======
Morning = "<ABSOLUTE PATH>1.jpeg" #Morning image
Afternoon = "<ABSOLUTE PATH>2.jpeg" #Afternoon image
Evening = "<ABSOLUTE PATH>3.jpeg" #Evening image
Night = "<ABSOLUTE PATH>4.jpeg" #Night image
>>>>>>> 474763a76e0cec01b5aac5f4b93fee953ed835ef

t = win10toast.ToastNotifier() #TO DISPLAY TOAST NOTIFICATIONS


#TO START ON BOOT.
def addStartup():  
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = reg.OpenKey(reg.HKEY_CURRENT_USER, keyVal, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key2change, 'PresenceDWP', 0, reg.REG_SZ,new_file_path)


#VALIDATION AND VERIFICATION
if os.path.isfile('./LICENSE') == True:
	if os.path.isfile('./DONTDELETE.txt') == True:
		pass
	else:
		with open('DONTDELETE.txt','w+') as file:
			file.write("Quit deleting me!")
			file.close()
		addStartup()
else:
	t.show_toast('PresenceDWP','Get the LICENSE from GitHub Repo and try again!','toast.ico',duration=10) #Notify with Custom Icon


#TO CHANGE THE WALLPAPER
def change():
	T = int(datetime.now().strftime('%H')) #In 24hr format. Type casted this into integer(String by default)
	#Anytime before noon
	if T < 12:
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Morning, 0) #Setting the Morning image as wallpaper
		print("Changed to Morning") #Debugging!
		t.show_toast('PresenceDWP','Good Morning!','toast.ico',duration=10) #Notify with Custom Icon
	#From noon to 5PM
	elif T in range(12,17):
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Afternoon, 0) #Setting the Afternoon image as wallpaper
		print("Changed to Afternoon") #Debugging!
		t.show_toast('PresenceDWP','Good Afternoon!','toast.ico',duration=10) #Notify with Custom Icon
	#From 5PM to 8PM
	elif T in range(17,20):
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Evening, 0) #Setting the Evening image as wallpaper
		print("Changed to Evening") #Debugging!
		t.show_toast('PresenceDWP','Good Evening!','toast.ico',duration=10) #Notify with Custom Icon
	#After 8PM till midnight!
	else:
		ctypes.windll.user32.SystemParametersInfoW(20, 0, Night, 0) #Setting the Night image as wallpaper
		print("Changed to Night") #Debugging!
		t.show_toast('PresenceDWP','Are you a night owl?','toast.ico',duration=10) #Notify with Custom Icon

#While loop to keep the script alive in the background
while True:
<<<<<<< HEAD
	change() #Will check the time and change the wallpaper every 3 hours
	time.sleep(10800) #Sleep for 3hrs
	
=======
	schedule.every(3).hours.do(change) #Will check the time and change the wallpaper every 3 hours
	
>>>>>>> 474763a76e0cec01b5aac5f4b93fee953ed835ef
