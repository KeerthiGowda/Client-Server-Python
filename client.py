import socket

def Main():
	
	# Get name and port number of the server
	host = input("Enter the name of the host : ")
	portnumber = input("Enter the port number at which host is running : ")
	port = int(portnumber)

	# Create Socket
	s = socket.socket()
	s.settimeout(2)
	
	# Connect to server
	s.connect((host,port))

	# Get the filename from the user to be searched on server
	filename = input("Enter the Filename to be search on the server : ")
	command = "GET " + filename + " HTTP/1.0"
	
	# Print the HTTP Get command
	print (command)
	
	# Send the command to socket
	s.send(str.encode(command))
	
	# Receive the command sent to socket
	data = s.recv(1024)
	
	print (data)
	
	datafinal = data.decode()
	print('datafinal' + datafinal)

	data = s.recv(1024)
	
	stringdecode = data.decode()
	print ('Contents of the file are :  ' + stringdecode)

	# Copy the contents into the new file
	f = open('new_'+filename, 'wb')
	
	breaker = 1
	while (len(stringdecode)>0 and breaker <=5):
		f.write(data)
		try:
			data = s.recv(1024)
			stringdecode = data.decode()
		except:
			strdecode = ""
		breaker+=1
	
	# Close the file
	f.close()
	print ("Download Complete!")
	
	# Close the socket
	s.close()

def ActualMain():
	Main()
	Main()
	Main()

if __name__ == '__main__':
	ActualMain()
