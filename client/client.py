import socket
import threading
import random
import string
import pyautogui
import time

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
    return "".join(random.choice(list(string.ascii_lowercase)))


def convert_to_morse_code(message):
    return "".join(letters[character] + (" " if character != "/" else "") for character in message.lower())


def play_morse_code(message):
    playing = False
        
    for character in message:
        play = False if character == "/" or character == " " else True
        sleep_time = DIT_MS if character == "." else DIT_MS * 7 if character == "/" else DIT_MS * 3

        if play or not play and playing:
            pyautogui.press("space")
            playing = not playing
                
        time.sleep(sleep_time / 1000)
        pyautogui.press("space")


DIT_MS = 100


def recieved_message_handler(s):
    in_window = True
    
    while True:
        message = s.recv(1024).decode()
        
        if not in_window:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
            in_window = True
        
        print("Message", message)
        play_morse_code(message)


def main():
    s = socket.socket()
    s.connect(("localhost", int(input("Enter a port: "))))

    recieving_thread = threading.Thread(
        target=recieved_message_handler, args=(s,)
    ).start()

    while True:
        message = convert_to_morse_code(input(""))

        if message:
            try:
                s.send(message.encode())
            except Exception as e:
                s.close()
                break


if __name__ == "__main__":
    main()
