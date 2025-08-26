import socket

server_port=8080
format = 'utf-8'
buffer_for_message_length = 16

#create the servers address
hostname= socket.gethostname()
host_ip= socket.gethostbyname(hostname)
addr= (host_ip,server_port)

# create a socket for the client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

server.listen() 
print("Server is listening")
while True:
    conn,add=server.accept()
    print(f"Connection established with {add}")
    
    connected=True
    while connected:
        message_length= conn.recv(buffer_for_message_length).decode(format)
        print("Upcoming message length:", message_length)

        if message_length:
            message_length= int(message_length)
            message= conn.recv(message_length).decode(format)
            
            if message == "Disconnect":
                connected = False
                print("Terminating connection with ",add)
                conn.send("The session is terminated".encode(format))
                print("\n")
            else:
                print(message)
                conn.send("The server has received the message".encode(format))
                print("\n")
            
    conn.close()
    
