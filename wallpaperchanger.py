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

pathToBmp = "YOUR_PATH_\\this.jpg" #Update your path here.
SPI_SET_WALLPAPER = 20 #You could just type in 20 below to save a variable.
ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, pathToBmp, 0) #Using the DLL to set the wallpaper.