#!/usr/bin/python3

import socket 

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 'ipaddress'
host = socket.gethostname()

port = 444 #Choose a port number. 

clientsocket.connect(('ipaddress', port))

#Buffersize = maximum amount of data allowed to come through TCP.
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
