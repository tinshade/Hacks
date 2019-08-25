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
import emoji #Just to add some fun stuff. I recommend using VSCode.


pwd = os.path.dirname(os.path.realpath(__file__)) #Present working diretory.
#wrkdir = pwd #Setting the working directory to 'pwd' by default.
temp = os.path.split(pwd) #Splitting the path to get the path and folder name seperately.



'''

FUNCTION TO CREATE REACT PROJECT

'''
def create_react(chosendir):
	#Added try-catch block to catch errors.
	try:
		proj_name = input("What would you like to call your new React project? \n") #Variable for project's name
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
		print(ret) #Print result after cmd execution

		#If the command succeeds with 0, we are through.
		if ret == 0:
			print(emoji.emojize("Your project is ready with a starter boiler-plate!\n HAPPY HACKING :grinning_face_with_big_eyes:"))
			#Printing the success message with classic ending line from react commandline

	except FileExistsError:
		print("Oops, looks like this project directory already exists.\nTry deleting the directory or choose a diffrent name") #Handling the known exception raised by os module
		exit() #Quitting. I will make this loop in future release.



'''

FUNCTION TO CHECK THE DIRECTORIES

'''
def precheck(value):
	#value variable has the path chosen by the user. Either default given by me or project folder default or, finally, the chosen path.
	#Check if the path given exists or not.
	if os.path.exists(value):
		print('Great! This already exists!\n') #Confirm that path exists
		create_react(value) #Calling the react function
	else:
		print('Looks like this path does not exists. Initializing the path...\n') #Display path not found!
		os.mkdir(value) #Make the directory 
		create_react(value) #Calling the react function




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
		if chdir.upper() =="N":
			#Choosing N means you are not satisfied with the displayed directory and wish to change the project's root directory for this run only.
			new_dir = input("Enter the new directoy: ") #Asking for new directory for this instance only.
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
			print("You default projects root directory has been set to {}.\nChange it anytime in the config.txt manually.".format(wrkdir)) #Display confirmation
			config.write(user_name + "\n" + wrkdir) #Writing the default path to config.txt file
			config.close() #Closing the file.

main() #Calling the MAIN function


#CMD Command to create the project and install npm
#cd <path> && create-react-app <app_name> && cd <app_name> && npm install