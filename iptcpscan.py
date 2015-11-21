import socket
from datetime import datetime

net = raw_input("Enter the IP Address ")
net2 = net
print net2
st1 = int(raw_input("Enter Starting number "))
en1 = int(raw_input("Enter the last number "))
en1 = en1 + 1

t1 = datetime.now()
def scan(addr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	print addr
	result = sock.connect_ex((addr, 80))
	if result == 0:
		return 1
	else:
		return 0

def run1():
	for ip in xrange(st1, en1):
		addr = net2+'.'+str(ip)
		if (scan(addr)):
			print addr, "is live"

run1()
t2 = datetime.now()
total = t2 - t1
print "scanning complete in ", total
