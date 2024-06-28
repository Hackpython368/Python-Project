import time 
from tkinter import *


def Time():
    currenttime = time.strftime("%I:%M:%S %p")
    TimeLabel.config(text=currenttime)
    App.after(1,Time)

App = Tk()

App.title("Clock")

App.geometry('440x80')

Frame1 = Frame(App)
Frame2 = Frame(App)
TimeLabel = Label(Frame2,foreground="red",background= "black",font=("arial",52))
ItemsLabel = Label(Frame1,background="black")
Button1 = Button(ItemsLabel,text="Alarm",foreground="white",background="black").pack()
Button1 = Button(ItemsLabel,text="",foreground="white",background="black").pack()
ItemsLabel.pack(ipady = "14")
Time()
TimeLabel.pack()


Frame1.grid(row=0,column=0)
Frame2.grid(row=0,column=1)
App.mainloop()
