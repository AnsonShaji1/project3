import socket
import re

host = '127.0.0.1'
port = 4545
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) 
print("Waiting for connecting");

while True:
	csock, caddr = sock.accept()
	print "Connection from: " +str(caddr)
	req = csock.recv(1024) 
	print req
	if(re.match('GET /text HTTP/1', req)):
		csock.sendall("""HTTP/1.0 200 OK
		Content-Type: text/html

		<html>
		<head>
		<title>Text</title>
		</head>
		<body>
		haiiii!!!
		</body>
		</html>
		""")
    	elif(re.match('GET /img HTTP/1', req)):
		csock.sendall("""HTTP/1.0 200 OK
		Content-Type: image/jpeg

		<html>
		<head>
		<title>Images</title>
		</head>
		<body>
		<img src="/home/jishnu/Desktop/anson.jpg" alt="ANSON" style="width:304px;height:228px;">
		</body>
		</html>
		""")
	else:
		print("Returning 404")
		csock.sendall("HTTP/1.0 404 Not Found \n")
	csock.close()
