import socket

server_port=8080
format = 'utf-8'
buffer_for_message_length = 1024

#create the servers address
hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
addr= (host_ip,server_port)

# create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(addr)

