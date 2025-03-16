import socket

s = socket.socket()
s.connect(("localhost", 12345))

letters = { "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ". ", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---", "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "...", "t" : "-", "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..", " " : "/"}

def convert_to_morse_code(message):
    return "".join(f"{letters[character.lower()]} " for character in message)

while True:
    message = input("Enter a message: ")
    if message:
        try:
            s.send(message.encode())
        except Exception as e:
            s.close()
            break
    
    print(s.recv(1024).decode())