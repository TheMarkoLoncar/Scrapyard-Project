letters = { "a" : ".- ", "b" : "-... ", "c" : "-.-. ", "d" : "-.. ", "e" : ". ", "f" : "..-. ", "g" : "--. ", "h" : ".... ", "i" : ".. ", "j" : ".--- ", "k" : "-.- ", "l" : ".-.. ", "m" : "-- ", "n" : "-. ", "o" : "--- ", "p" : ".--. ", "q" : "--.- ", "r" : ".-. ", "s" : "... ", "t" : "- ", "u" : "..- ", "v" : "...- ", "w" : ".-- ", "x" : "-..- ", "y" : "-.-- ", "z" : "--.. ", " " : "/ "}

input = ("I enjoy touching kids").lower()


for character in input:
    print(letters[character], end="")

