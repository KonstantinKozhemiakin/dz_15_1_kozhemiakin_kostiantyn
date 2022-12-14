import socket
import myloger


if __name__ == "__main__":
    logger = myloger.init_my_loger()
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 55000
    logger.info(f'This is your IP address:{ip}')
    # print('This is your IP address: ', ip)
    name = input('Enter your name: ')

    socket_server.connect((server_host, sport))

    socket_server.send(name.encode())
    server_name = socket_server.recv(1024)
    server_name = server_name.decode()
    # print(server_name, ' has joined...')
    logger.warning(f'{server_name} has joined...')
    try:
        while True:
            message = input("Me : ")
            socket_server.send(message.encode())
            message = (socket_server.recv(1024)).decode()
            print(server_name, ":", message)
        # socket_server.close()
    except:
        logger.error('There is no connection to the server')
        socket_server.close()
        logger.error('Client socket close')
