import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '10.0.0.167'
port = 12345
s.connect((host, port))
msg = s.recv(1024)
print msg
print struct.unpack('hhl', msg)
s.close()
