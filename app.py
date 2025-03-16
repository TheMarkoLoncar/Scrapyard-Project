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
                compound='top'
                )

#text
text1 = Label(window,
                text="Enter text to translate:",
                font=("MS Sans Serif", 12),
                fg="black",
                bg="white"
              )

#text box
text_to_translate = Entry(window,
                          font=("MS Sans Serif", 12)
                          )

#this is what makes the text appear
heading.pack()
text1.place(x=10, y=75)

#this is what the translator will port into
def click():
    pass


window.mainloop()