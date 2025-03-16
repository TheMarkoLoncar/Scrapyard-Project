from tkinter import *

window = Tk()
window.title("morse code translator")
window.geometry("500x500")
window.config(bg="white")

#text header
heading = Label(window,
                text="Morse Code Translator lol",
                font=("MS Sans Serif", 20, 'bold'),
                fg="black",
                bg="white",
                )
#this is what makes the text appear
heading.pack()

#this is what the translator will port into
def click():
    pass


window.mainloop()