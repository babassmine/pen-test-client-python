import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.0.0.167" # server address
port = 12345 # server port

s.connect((host,port)) # connect to server
print s.recv(1024) # recieve 1024 byte from server 
s.send ("Hello Server")
s.close()

