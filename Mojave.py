"""
	THE MOJAVE WALLPAPER EFFECT

	Setting dynamic time-based wallpapers like in 
	Mac OS's Mojave update

	
"""
import ctypes #To change the wallpaper
from datetime import datetime #To know what time it is


T = int(datetime.now().strftime('%H')) #In 24hr format. Type casted this into integer(String by default)

#Image paths
Morning = "<ABSOLUTE_PATH>\\1.jpeg" #Morning image
Afternoon = "<ABSOLUTE_PATH>\\2.jpeg" #Afternoon image
Evening = "<ABSOLUTE_PATH>\\3.jpeg" #Evening image
Night = "<ABSOLUTE_PATH>\\4.jpeg" #Night image

#Anytime before noon
if T < 12:
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Morning, 0) #Setting the Morning image as wallpaper
	print("Changed to Morning") #Debugging!
#From noon to 5PM
elif T in range(12,17):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Afternoon, 0) #Setting the Afternoon image as wallpaper
	print("Changed to Afternoon") #Debugging!
#From 5PM to 8PM
elif T in range(17,20):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Evening, 0) #Setting the Evening image as wallpaper
	print("Changed to Evening") #Debugging!
#After 8PM till midnight!
else:
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Night, 0) #Setting the Night image as wallpaper
	print("Changed to Night") #Debugging!