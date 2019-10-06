'''

	AUTO-TEMPLATE
	Author : Abhishek Iyengar
	GitHub: https://github.com.tinshade

	ABOUT:
	I created this script to automate the generation of boiler-plates and other templates for 
	programming frameworks that I use.

	Although its exciting to create a project from the commandline, it isn't as fun when you're
	testing/going through tutorial-hell making 2-3 projects per day.

	So here's a way that will remain fun for a while.


	NOTE: This project is not 'complete' but its still functional. 
	The main idea was to make it a voice activated "software" if you may, that awaits your commands.
	This version only includes React based commmand for now. I might add a few like Laravel and Django
	soon, along with an ElectronJS wrapper.

'''
import os #To make use of OS based commands(Make Files and Directories.)
import subprocess #Calling the CMD subprocesses safely.
from subprocess import Popen, CREATE_NEW_CONSOLE #To open a new CMD window
import emoji #Just to add some fun stuff. I recommend using VSCode.
import webbrowser #To run chrome after opening the server.
from multiprocessing import Process
#from subprocess import Popen, CREATE_NEW_CONSOLE #Creates a subprocess shell call from Python Shell (Visible only from task manager)


pwd = os.path.dirname(os.path.realpath(__file__)) #Present working diretory.
#wrkdir = pwd #Setting the working directory to 'pwd' by default.
temp = os.path.split(pwd) #Splitting the path to get the path and folder name seperately.


'''

FUNCTION TO OPEN LOCAL HOST FOR DJANGO (Parallel Processing)

'''
def django_server():
	webbrowser.open_new("http://localhost:8000")  #Opening new Chrome instance at the default web-address for Django projects
	print(emoji.emojize("Your project is ready with a starter boiler-plate!\n I HOPE YOU MEET YOUR DEADLINE :grinning_face_with_big_eyes:"))#Printing the success message with classic ending line from react commandline




'''

FUNCTION TO CREATE REACT PROJECT

'''
def create_react(chosendir):
	#Added try-catch block to catch errors.
	try:
		proj_name = input("What would you like to call your new React project? \n") #Variable for project's name
		if "C:\\" in proj_name:
			print("Can't do that in the OS drive. Please choose some other partition/drive or destination")
			proj_name = input("What would you like to call your new React project? \n") #Re-assign after catching the error
		else:
			new_path = chosendir + '/' + proj_name #Append the chosen directory path with the project folder's name
			print('\n{}!\nCool Name!'.format(proj_name)) #Display confirmation
			print('This will be the directory path for your new project:', new_path) #Display path confirmaton
			'''

				The 'cmd' is the CMD command with chaining that performs the core action.
				DO NOT CHANGE IT IF YOU DON'T KNOW WHAT YOU'RE DOING!


			'''
			cmd = "cd {0} && create-react-app {1} && cd {1} && npm install".format(chosendir,proj_name.lower()) #React projects cant have captialized names.
			print("This will take a while. I will notify you when I'm done...") #Notify aboout the wait time.
			ret = subprocess.call(cmd, shell=True) #Run the shell command with subprocess call for safety and store the return value. 0 = Success and 1 = Failure
			#print(ret) #Print result after cmd execution #DEBUGGING

			#If the command succeeds with 0, we are through.
			if ret == 0:
				print(emoji.emojize("Your project is ready with a starter boiler-plate!\n HAPPY HACKING :grinning_face_with_big_eyes:"))
				#Printing the success message with classic ending line from react commandline

	except FileExistsError:
		print("Oops, looks like this project directory already exists.\nTry deleting the directory or choose a diffrent name") #Handling the known exception raised by os module
		exit() #Quitting. I will make this loop in future release.

'''

FUNCTION TO CREATE DJANGO PROJECT

'''
def create_django(chosendir):
	try:
		proj_name = input("What would you like to call your new Django project? \n") #Variable for project's name
		if "C:\\" in proj_name:
			print("Can't do that in the OS drive. Please choose some other partition/drive or destination")
			proj_name = input("What would you like to call your new React project? \n") #Re-assign after catching the error
		else:
			if proj_name == "test":
				print("Since 'test' is a python keyword and can not be used as a project name. Please try some other name")
				proj_name = input("So, what would you like to call your new Django project? \n") #Variable for project's name
			else:
				pass

		new_path = chosendir + '/' + proj_name #Append the chosen directory path with the project folder's name
		app_name = input("And your app's name? \n") #Variable for app's name
		print('\n {}!\nGood job!'.format(app_name)) #Display confirmation
		print('This will be the directory path for your new project:', new_path) #Display path confirmaton
		'''

			The 'cmd' is the CMD command with chaining that performs the core action.
			DO NOT CHANGE IT IF YOU DON'T KNOW WHAT YOU'RE DOING!


		'''
		print("This will take a while. I will make migrations and spin up the server when I'm done...") #Notify aboout the wait time.
		cmd1 = "cd {0} && django-admin startproject {1} && cd {1} && django-admin startapp {2}".format(chosendir,proj_name,app_name)
		ret = subprocess.call(cmd1, shell=True) #Run the shell command with subprocess call for safety and store the return value.
		if ret == 0:
			cmd2 = "cd {0} && cd {1} && python manage.py makemigrations && python manage.py migrate && python manage.py runserver".format(chosendir,proj_name)
			#subprocess.Popen(cmd2, shell=True, creationflags=CREATE_NEW_CONSOLE) #Run the shell command with subprocess call for safety and store the return value.
			#webbrowser.open_new("http://localhost:8000")  #Opening new Chrome instance at the default web-address for Django projects
			#print(emoji.emojize("Your project is ready with a starter boiler-plate!\n I HOPE YOU MEET YOUR DEADLINE :grinning_face_with_big_eyes:"))#Printing the success message with classic ending line from react commandline
			Process(target = django_server).start()
			subprocess.call(cmd2, shell=True) #Run the shell command with subprocess call for safety and store the return value.
		else:
			print("Something went wrong while creating the project. Please re-run the script")
			quit()
		
		

	except FileExistsError:
		print("Oops, looks like this project directory already exists.\nTry deleting the directory or choose a diffrent name") #Handling the known exception raised by os module
		quit() #Quitting. I will make this loop in future release.


'''

FUNCTION TO CREATE FLUTTER PROJECT

'''
def create_flutter(chosendir):
	try:
		proj_name = input("What would you like to call your new flutter project? \n") #Variable for project's name
		if "C:\\" in proj_name:
			print("Can't do that in the OS drive. Please choose some other partition/drive or destination")
			proj_name = input("What would you like to call your new React project? \n") #Re-assign after catching the error
		else:
			if proj_name == "_":
				print("Please try some other name")
				proj_name = input("So, what would you like to call your new Django project? \n") #Variable for project's name
			else:
				pass

		new_path = chosendir + '/' + proj_name #Append the chosen directory path with the project folder's name
		print('\n {}!\nGood job!'.format(proj_name)) #Display confirmation
		print('This will be the directory path for your new project:', new_path) #Display path confirmaton
		'''

			The 'cmd' is the CMD command with chaining that performs the core action.
			DO NOT CHANGE IT IF YOU DON'T KNOW WHAT YOU'RE DOING!


		'''
		print("This will take a while...") #Notify aboout the wait time.
		print(emoji.emojize(":grinning_face_with_big_eyes:"))
		cmd1 = "cd {0} && flutter create {1} && cd {1}".format(chosendir,proj_name)
		ret = subprocess.call(cmd1, shell=True) #Run the shell command with subprocess call for safety and store the return value.
		if ret == 0:
			cmd1 = "cd {0}/{1}".format(chosendir,proj_name)
			subprocess.call(cmd1, shell=True)
		else:
			print("Something went wrong while creating the project. Please re-run the script")
			quit()
	except FileExistsError:
		print("Oops, looks like this project directory already exists.\nTry deleting the directory or choose a diffrent name") #Handling the known exception raised by os module
		quit() #Quitting. I will make this loop in future release.

'''

FUNCTION TO CHECK THE DIRECTORIES

'''
def precheck(value):
	#value variable has the path chosen by the user. Either default given by me or project folder default or, finally, the chosen path.
	#Check if the path given exists or not.
	value = value.replace(" ","") #Removing whitespaces for mkdir (White-Spaces will create separate directory for each word)
	if os.path.exists(value):
		print('Great! This already exists!\n') #Confirm that path exists
		proj_type = input("What project this time?\nOptions : 1. React || 2.Django || 3.Flutter \n")
		if proj_type == "1":
			print("React Project")
			create_react(value) #Calling the react function
		elif proj_type == "2":
			print("Django Project")
			create_django(value) #Calling the django function
		elif proj_type == "3":
			print("Flutter Project")
			create_flutter(value) #Calling the flutter function
		else:
			print("Please select 1 for React and 2 for Django and 3 for Flutter!\nSelecting invalid values ain't cool, man!")
	else:
		print('Looks like this path does not exists. Initializing the path...\n') #Display path not found!
		os.mkdir(value) #Make the directory 
		proj_type = input("What project this time?\nOptions : 1. React || 2.Django || 3.Flutter \n")
		if proj_type == "1":
			create_react(value) #Calling the react function
		elif proj_type == "2":
			create_django(value) #Calling the django function
		elif proj_type == "3":
			create_flutter(value) #Calling the flutter function
		else:
			print("Please select 1 for React and 2 for Django and 3 for Flutter!\nSelecting invalid values ain't cool, man!")




'''

THE MAIN FUNCTION

'''

def main():
	'''
	
			THE 'config.txt' FILE CONSISTS OF THE USER'S NAME AND THE DEFAULT DIRECTORY.
			THIS FILE IS CREATED UPON FIRST BOOT AND IS USED THROUGHOUT THE APPLICATION.

			EDIT THIS ONLY IF YOU KNOW WHAT YOU ARE DOING. IT'S SIMPLE TBH...

			THIS WILL BE CHANGED INTO A JSON FILE IN THE FUTURE RELEASE WITH MUCH MORE VALUE
			THAN TO JUST HOLD A COUPLE OF DATA STRINGS.

	'''
	#If this does not exists, it will be treated as inital boot.
	if os.path.exists('config.txt'):
		#Opening the file to read contents with config variable
		with open('config.txt','r') as config:
			info = config.readlines() #Reading the file line by line to form an array.
			user_name = (info[0]) #Username from line one.
			proj_dir = (info[1]) #Default path from line two.
		
		print("Welcome back, {0}\nYour current project directory is {1}".format(user_name, proj_dir)) #Confirming username and path with welcome message.
		chdir = input("Would you like to continue with this ?\nEXPECTING Y/N\n")  #Asking for change of directory before starting the build.

		#Chaning the input to upper to match the test case.
		if chdir.upper() == "N":
			#Choosing N means you are not satisfied with the displayed directory and wish to change the project's root directory for this run only.
			new_dir = input("Enter the new directoy: ") #Asking for new directory for this instance only.
			if "C:\\" in new_dir:
				print("Can't do that in the OS drive. Please choose some other partition/drive or destination")
				new_dir = input("Enter the new directoy: ") #Re-assinging values again after error
			else:
				pass
			temp = new_dir #Changing the global variable's value to new value only for this instance.
			print("Changed the working directory to {}!".format(temp)) #Display change confirmation
			precheck(temp) #Passing the chosen directory to the checker function above.
		else:
			precheck(proj_dir) #Passing the default/ initially chosen directory to the checker function above.			
	else:
		print('Welcome to AutoScripts. We see this is your first time here! \n Setting things up...\n') #Display intro message on initial boot if the config.txt is not found.
		config = open('config.txt','w+') #Creating the config.txt with write mode.
		user_name = input('What do I call you?\n') #Asking for user name
		default_dir = input('Do you wish to set up a default root directory for you projects?\nEXPECTING Y/N \n') #Asking for default directory for all future projects
		if default_dir.upper() == "N":
			#Answering N will set the default to current directory
			default_dir = pwd #Setting the default for all future projects to the present working directory.
			config.write(default_dir+"\n") #Writing the default path to config.txt file.
			#print(default_dir) #DEBUGGING: Checking if the correct path was written.
			config.close() #Closing the file.
		else:
			#Answering Y will ask for a path to be set as default for all future projects.
			wrkdir = input('Enter the root directory\n') #Asking for default path.
			if "C:\\" in wrkdir:
				print("Can't do that in the OS drive. Please choose some other partition/drive or destination")
				wrkdir = input('Enter the root directory\n') #Asking for default path.
			else:
				pass
			print("You default projects root directory has been set to {}.\nChange it anytime in the config.txt manually.".format(wrkdir)) #Display confirmation
			config.write(user_name + "\n" + wrkdir) #Writing the default path to config.txt file
			config.close() #Closing the file.

main() #Calling the MAIN function


#CMD Command to create the project and install npm
#cd <path> && create-react-app <app_name> && cd <app_name> && npm install