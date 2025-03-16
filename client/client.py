import socket
import threading
import random
import string
import time
import pyaudio
import wave

letters = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
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
    "": "",
}


playing = False
wf = wave.open("never.wav")
pa = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)


stream = pa.open(
    format=pa.get_format_from_width(wf.getsampwidth()),
    channels=wf.getnchannels(),
    rate=wf.getframerate(),
    output=True,
    stream_callback=callback,
    start=False
)


def toggle_audio():
    global playing
    playing = not playing

    if playing:
        stream.start_stream()
    else:
        stream.stop_stream()


def get_random_letter():
    return "".join(random.choice(list(string.ascii_lowercase)))


def convert_to_morse_code(message):
    return "".join(letters[character] + " " for character in message.lower())


DIT_MS = 100
DAH_MS = DIT_MS * 3
SPACE_MS = DIT_MS * 7


def play_morse_code(message):
    global playing

    for character in message:
        if character == " ":
            continue

        play = False if character == "/" else True
        play = play or not play and playing
        play_time = DIT_MS if character == "." else DAH_MS if character == "-" else 0
        sleep_time = SPACE_MS if character == "/" else DAH_MS

        if play:
            toggle_audio()
        time.sleep(play_time / 1000)
        if play:
            toggle_audio()
        time.sleep(sleep_time / 1000)

    if playing:
        toggle_audio()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recieved_message_handler():
    while True:
        message = s.recv(1024).decode()

        print("Message", message)
        play_morse_code(message)


def setup_recieving():
    global s
    s.connect(("172.20.10.3", 6969))

    recieving_thread = threading.Thread(
        target=recieved_message_handler
    ).start()
