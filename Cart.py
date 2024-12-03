from tkinter import * 

a = 0

def showQuantity():
    Lable1.config(text=f"{a}")

def addTocart():
    global a
    a += 1

def add2():
    global a
    a += 2

def add3():
    global a
    a += 3

def reset():
    global a
    a = 0


app = Tk()
button1 = Button(app,text="Show Quantity",width=10,command=showQuantity)
button1.pack()

button2 = Button(app,text="Add To Cart",width=10,command=addTocart)
button2.pack()
button3 = Button(app,text="+2",width=10,command=add2)
button3.pack()
button4 = Button(app,text="+3",width=10,command=add3)
button4.pack()
button5 = Button(app,text="Reset",width=10,command=reset)
button5.pack()

Lable1 = Label(app,width=10)
Lable1.pack()
app.mainloop()
