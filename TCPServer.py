#!/usr/bin/python3

#Imported socket module
import socket

#Serversocket= creation of the socket object.
#AF_INET due to the fact that we will be utilizing connection-based protocols (TCP) that will be based on performing the 3-way handshake before initiating connections. 
#Specified socket type as well as family.
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ip() #Host is the server IP address. // Automation of obtaining IP address of the host/server. // Host = 192.168.1.67.
port = 444 #Port to listen on. You can customize this to your liking. 

#Binding to socket (socket object created above) / Replace host and port with IP address of host. / Port does not have to be changed as it was denoted above.  
serversocket.bind(('ip', port))

#TCP Listener started ; Amount of connections permitted (current=3 connections).
serversocket.listen(3)

#While true, the client socket and address will accept the TCP information coming from the client. 
while true:
    #Starting the connection
    clientsocket, address = serversocket.accept()

    print("Received connection from %s" % str(address)) 

    #The message sent to client after successful connection "\r\n" = ends and goes to next line. 
    message = 'Connected to the server' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()