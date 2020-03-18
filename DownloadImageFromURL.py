"""
	URL IMAGE DOWNLOADER
	Author: Abhishek Iyengar
	Github: @tinshade
	YT: https://youtube.com/AnnoyingErrors41
	DISCLAIMER: I DO NOT OWN ANY OF THE IMAGES MIGHT BE DOWNLOADED USING THIS SCRIPT! USE AT YOUR OWN RISK!


	This script can download an image from any given url. If the URL is not functional, it downloads a random image from
	Unsplash instead as a fallback code.

	This script is a small module to the Wallpaper Changer script that can be found here:
	https://github.com/tinshade/Hacks/blob/WallpaperChanger/wallpaperchanger.py
"""


import requests
from datetime import datetime

#Here's a random picture for URL if you want to test it out:
#pic_url = "https://source.unsplash.com/random"
def custom():
	with open(filename+'.jpg', 'wb') as handle:
		response = requests.get(pic_url, stream=True)
		if not response.ok:
			print(response)
		else:
			print("Downloaded")
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)

def fallback():
	with open(filename+'.jpg', 'wb') as handle:
		pic_url = "https://source.unsplash.com/random"
		response = requests.get(pic_url, stream=True)
		if not response.ok:
			print(response)
		else:
			print("Your URL was not working so I downloaded a random image instead!")
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)


def main():
	try:
		custom()
	except Exception as e:
		fallback()
pic_url = str(input("Enter an Image URL: "))
now = datetime.now()
filename = now.strftime("%d%m%Y%H%M%S")

main()