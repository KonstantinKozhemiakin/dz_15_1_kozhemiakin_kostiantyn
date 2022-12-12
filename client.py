import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 55000

print('This is your IP address: ', ip)
name = input('Enter your name: ')

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, ' has joined...')
while True:
    message = input("Me : ")
    socket_server.send(message.encode())
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
socket_server.close()
