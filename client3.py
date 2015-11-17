import socket

host = "10.0.0.167"
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
buf = bytearray("-" * 30 ) #buffer created
print "Number of Bytes ", s.recv_into(buf)
print buf
s.close()
