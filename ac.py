from tkinter import *
from tkinter import ttk
import pydirectinput
import time
from time import sleep
import keyboard
import threading

app = Tk()
app.geometry('400x350')

def start_def():
    while True:
        clickspeed = clickinput.get()
        keyboardb = keyinput.get()
        if keyboard.read_key() == keyboardb:
            pydirectinput.PAUSE = float(clickspeed)
            pydirectinput.click()

app.title("Calm")
app.configure(background="black")

txtspeed = Label (app, text="Voice Changer Pitch \n1 is 1 Pitch/s\ntype lower for more\nExample: 0.1", bg="black", fg="white", font="none 12 bold")
txtspeed.pack()

clickinput = Entry(app, width = 30)
clickinput.pack()

txtkey = Label (app, text="The button that toggles the voice changer \n(only you can hear it)\nMade for recording, not discord calls", bg="black", fg="white", font="none 12 bold")
txtkey.pack(pady=10)

keyinput = Entry(app, width = 30)
keyinput.pack()

startbutton = ttk.Button(app, text="Start", command=threading.Thread(target=start_def).start())
startbutton.pack(pady=30)

stopbutton = ttk.Button(app, text="Panic", command=app.destroy)
stopbutton.pack(pady=2)

app.mainloop()