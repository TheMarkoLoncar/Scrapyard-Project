import socket
import threading
import re

connections = []


def close_connection(connection):
    connection.close()


def distribute_message(message, sender):
    for connection in connections:
        try:
            if connection == sender:
                continue

            connection.send(message.encode())
        except Exception as e:
            close_connection(connection)


def connection_handler(connection):
    while True:
        try:
            message = connection.recv(1024).decode()
            if not re.search("[-./]+", message):
                connection.send(
                    "Messages can only contain morse code!".encode()
                )
                continue

            print(f"Message from connection {connection}:", message)
            distribute_message(message, connection)
        except Exception as e:
            close_connection(connection)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")

def main():
    global s

    s.bind(("10.17.192.55", 6969))

    s.listen(5)
    print("socket is listening", s.getsockname())

    while True:
        c, addr = s.accept()
        connections.append(c)
        print(f"Got connection from", addr)

        connection_thread = threading.Thread(
            target=connection_handler, args=(c,)
        ).start()


if __name__ == "__main__":
    main()
