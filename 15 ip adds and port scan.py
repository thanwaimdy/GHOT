#15.1 ip address and port scan
# dr. AWH GHOT  
# date 270319  7:49pm

import socket
print(socket.gethostname())
print(socket.gethostbyname("www.google.com"))
print(socket.gethostbyname("www.greenhackersonline.com"))
print(socket.gethostbyname("www.google.com"))
print(socket.gethostbyname("www.facebook.com"))
print(socket.gethostbyname("www.firefox.com"))




#to find pc ip address
hostname = socket.gethostname()
try:
	ip_address = socket.gethostbyname_ex(hostname)
	print(ip_address)
	print(ip_address[2][0])
	print(str(ip_address))
	print("Ipv4 address is" +str(ip_address[2][0]))
except:
	print('error')

# to find Ipv6

try:
	ip_address = socket.gethostbyname(hostname)
	
	print("Ipv6 address is" +str(ip_address))
	#this function is not sure for Ivp6
except:
	print('error')


#15.2 ip address scan

try:
	socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = socket_obj.connect_ex(('172.20.10.1', 21)) # 21 is scan
	if result == 0:
		print('***********************************************')
		print("computer exists at ip_address: " , "172.20.10.1")
		print('***********************************************')
		print()
		socket_obj.close()

	else:
		print("ip_address" + ip + " is not active")

		print("ip_address" + "172.20.10.1" + " is not active")
		socket_obj.close()

except:
		print("error")




