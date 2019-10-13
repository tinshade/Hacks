'''

    AUTHOR : Abhishek Iyengar
    GITHUB: @tinshade
    LICENSE: GNU Public License


    ###### PLEASE ADD ME IN THE CREDITS SECTION IF YOU PLAN TO USE THIS ######

    #!ACTIVITY MONITOR FOR WINDOWS!#

    This is an activity monitor that tells you what activity is currently being performed on your windows machine.
    This is a smaller modolue of a lareger "Activity Tracker" Project that visualizes the time you have spent on 
    all your applications on a daily basis.

    This sub-module however, can be used as a spy-tool to monitor targets if used correctly.
    I have plans to make a remote tracker by extending this module in future releases


'''

import pygetwindow as gw #To get currently active window and all other related actions
import time #To add wait times


#TO GET THE WINDOW IN FOCUS!
def get_focus():
    in_focus = gw.getActiveWindow().title #Returns the title of the window in focus 
    #Special condition for Google Chrome
    #!Other browser support will be added soon!
    if "Google Chrome" in in_focus:
        s = [] #Empty list to be filled later
        s = in_focus.split("-") #Filling the list with values from the string fetched from 'in_focus'
        #!SPLITS ARE AS FOLLOWS
        #0 is python (Medium of Execution)
        #1 is the title on the window (Title of Tab)
        #2 is website name (Website Name)
        #3 is Google Chrome(Software Name)

        #Assigning seperate variables to each value in the above list to have more control over what is
        #being printed
        if len(s) == 3:
            TabTitle = s[1]
            Website = s[2]
            Browser = s[3]
            print(f"You are looking at {TabTitle} on {Website} using {Browser}") #Print the final output to screen with 'f' string
        else:
            print("You are looking at ", in_focus)
    
    #If the application is not Google Chrome
    else:
        a = [] #Empty list to be filled later
        a = in_focus.split("-") #Filling the list with values from the string fetched from 'in_focus'

        #Try Catch block to handle Array Out Of Range Errors during split
        try:
            #Special condition for VS Code
            #!Support for Sublime and Atom will be added later!
            if "Visual Studio Code" in in_focus:
                #!SPLITS ARE AS FOLLOWS
                #0 is the name of the file
                #1 is the name of the folder in workspace
                #2 is the name of the software
                File = a[0]
                Folder = a[1]
                Editor = a[2]
                print(f"You are editing {File} in folder {Folder} using {Editor}") #Print the final output to screen with 'f' string
            else:
                #!SPLITS ARE AS FOLLOWS
                #0 is the name of the file
                #1 is the name of the software
                File = a[0]
                Software = a[1]
                print(f"You are viewing {File} using {Software}") #Print the final output to screen with 'f' string
        except Exception:
            print("Current Activity: ", in_focus) #When Array error occours, just print the title given by 'in_focus'


if __name__ == "__main__":
    #Createing an infinite loop
    while True:
        get_focus() #Calling the function to get the in focus window!
        time.sleep(5) #Added wait time of 5 seconds
