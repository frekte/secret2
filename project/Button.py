from tkinter import *
from tkinter import messagebox
import winsound
import threading

test = Tk()
test.geometry("860x560")

def helloCallBack():
   msg=messagebox.showinfo( "Josh", "Whistle")

photo = PhotoImage(file= r"files\files\test.png")
B = Button(test, text ='test', image = photo, command = test.destroy).pack(side = TOP)

def play_sound():
    winsound.PlaySound("test.wav", winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

test.mainloop()