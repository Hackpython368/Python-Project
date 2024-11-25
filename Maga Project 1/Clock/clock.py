import time 
from tkinter import *


def Time():
    currenttime = time.strftime("%I:%M:%S %p")
    TimeLabel.config(text=currenttime)
    App.after(1,Time)

App = Tk()

App.title("Clock")

App.geometry('480x80')
App.resizable(False,False)

Frame2 = Frame(App)
TimeLabel = Label(Frame2,foreground="red",background= "black",font=("arial",52),width=12)
Time()
TimeLabel.pack()

Frame2.grid(row=0,column=1)
App.mainloop()