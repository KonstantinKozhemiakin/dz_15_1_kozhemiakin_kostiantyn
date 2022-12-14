import socket
import myloger

if __name__ == "__main__":
    logger = myloger.init_my_loger()
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)

    port = 55000

    new_socket.bind((host_name, port))
    # print("Binding successful!")
    # print("This is your IP: ", s_ip)
    logger.info("Binding successful!")
    logger.info(f'This is your IP address:{s_ip}')


    name = input('Enter your name: ')

    new_socket.listen(10)
    conn, add = new_socket.accept()
    # print("Received connection from ", add[0])
    logger.warning(f'Received connection from {add[0]}.')
    # print('Connection Established. Connected From: ', add[0])
    logger.warning(f'Connection Established. Connected From: {add[0]}')

    client = (conn.recv(1024)).decode()
    # print(client + ' has connected.')
    logger.warning(f'{client} has connected.')
    conn.send(name.encode())
    try:
        while True:
            message = conn.recv(1024)
            message = message.decode()
            print(client, ':', message)
            message = input('Me : ')
            conn.send(message.encode())
    except:
        logger.error('There is no connection to the client')
        new_socket.close()
        logger.error('Server socket close')

