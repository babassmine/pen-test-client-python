import socket
host = "10.0.0.167"
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print s.sendto("hello all", (host, port))
s.close()
