import ctypes
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename="\\this.jpg"
path = dir_path+filename
#print(path)
SPI_SET_WALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SET_WALLPAPER, 0, path, 0)
