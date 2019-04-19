import urllib3
import win32api
import time
import sys

http = urllib3.PoolManager()
try :
	r = http.request('GET', 'https://www.youtube.com/channel/UCoKvMf0XfGYSuujgL6dFSeA')
	if r.status == 200:
		win32api.MessageBox(0, 'You are connected to the Internet', 'Active', 0x00001000)
		time.sleep(1)
		sys.exit(0)
		
except urllib3.exceptions.MaxRetryError as e:
	#print(e) #Debugging
	win32api.MessageBox(0, 'You are not connected to the Internet', 'Inactive', 0x00001000)
	time.sleep(.20)
