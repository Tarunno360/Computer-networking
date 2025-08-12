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
                hours_work = int(message)
                total_salary = 0
                if hours_work <= 40 and hours_work >=0:
                    total_salary = hours_work * 200
                elif hours_work > 40 :
                    total_salary = 8000 + (hours_work - 40) * 300            
                conn.send(f'Your salary is {total_salary} TK caluculating the work'.encode(format))
    conn.close() 
    