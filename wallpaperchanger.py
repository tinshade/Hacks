'''

	THE WALLPAPER SHUFFLER
	Author: Abhishek Iyengar
	GitHub: https://github.com/tinshade/
	This Repository: https://github.com/tinshade/Hacks/tree/WallpaperChanger

	I wrote this script just for fun demonstration purposes.

	The virus version includes changing the wallpaper to something embarrassing and autohide itself upon run,
	along with running on boot everytime!

	Feel free to make changes and improvements!


'''
import ctypes #This provides C compatible datatypes and allows the use of DLL files. The 'user32.dll' in particular for this case.

path = "<ABSOLUTE_PATH>\\this.jpg" #Update your path here.
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) #Using the DLL to set the wallpaper.import ctypes
