import socket
import threading
import random

letters = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ". ",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
}


def get_random_letter():
    return "".join(random.choice(list(letters.values())))


def convert_to_morse_code(message):
    return random.choice(list(letters.values()))


s = socket.socket()
s.connect(("localhost", 12345))


def recieved_message_handler():
    while True:
        print(s.recv(1024).decode())


def main():
    recieving_thread = threading.Thread(target=recieved_message_handler).start()

    while True:
        message = input("")
        if message:
            try:
                s.send(message.encode())
            except Exception as e:
                s.close()
                break


if __name__ == "__main__":
    main()
