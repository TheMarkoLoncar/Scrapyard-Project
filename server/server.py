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


def main():
    s = socket.socket()
    print("socket successfully created")

    port = int(input("Enter a port: "))

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("localhost", port))
    print(f"socket binded to", port)

    s.listen(5)
    print("socket is listening")

    while True:
        c, addr = s.accept()
        connections.append(c)
        print(f"Got connection from", addr)

        connection_thread = threading.Thread(
            target=connection_handler, args=(c,)
        ).start()


if __name__ == "__main__":
    main()
