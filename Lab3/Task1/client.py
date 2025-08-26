import socket

server_port=8080
format = 'utf-8'
buffer_for_message_length = 16

#create the servers address
hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
addr= (host_ip,server_port)

# create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #bivinno info pay tcp protocol eisob ki hobe

client.connect(addr) 

def message_to_be_sent(message):
    msg= message.encode(format)
    msg_length= str(len(message))
    msg_length= msg_length.encode(format)
    
    padding=b" " * (buffer_for_message_length - len(msg_length))
    msg_length+= padding
    
    client.send(msg_length)
    client.send(msg)
    
    print(client.recv(2048).decode(format))
    
message_to_be_sent(f"Hostname:{hostname}, IP: {host_ip}")
message_to_be_sent("Disconnect")
    
    
    
    
    
