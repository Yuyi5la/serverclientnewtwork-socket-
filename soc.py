#!/bin/python3
import socket
host = '127.0.0.1'
port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
while True:
	communication_socket,address = server.accept()
	print(f"connected to {addres}")
	message = communication_socket.rev(1024).decode('utf-8')
	print(f"message from client is : {message}")
	communication_socket.send(f"got your message!thank u ".encode('utf-8'))
	communication_socket.close()
