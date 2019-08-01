'''
AUTHOR : ABHISHEK IYENGAR
GITHUB : https://github.com/tinshade
REPOSITORY : https://github.com/tinshade/Hacks
LICENSE : MIT
'''

import os #To interact with the OS and files

count = 1 #Starting filename count with 1 i.e. 1.jpg

#BEGIN FOR LOOP
for filename in os.listdir('C:\\Users\\Abhishek\\Desktop\\Renamer\\Images'):
	#print(filename) #Debugging

	#ADDING IF BLOCK TO SKIP THE PYTHON FILE.
	#THIS CAN BE AVOIDED BY ADDING CHILD DIRECTORY BUT THAT IS TOO MUCH FOR A QUICK SCRIPT!
	if filename == 'Renamer.py':
		os.rename(filename,'Renamer.py') #Renames the file as itself, basically skipping it.
	else:
		os.rename(filename,str(count)+'.jpg') #Rename the current file with the number in count variable and add .JPG extension
		count += 1 #Increase the count by 1

print("[+] Renaming done.") #Success message

#PS. This also renames this file. You will have to add it as a child directory if you want to reuse without renaming the file itself.