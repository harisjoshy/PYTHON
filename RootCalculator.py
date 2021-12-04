
from tkinter import *
root= Tk()

root.title("Simple Calculator")

e = Entry(root, width= 50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3,pady=10)

def buttonClick(num):
    curr = e.get()
    e.delete(0, END)
    e.insert(0, str(curr) + str(num))

def Clear():
    e.delete(0,END)

def add():
    first_number = e.get()
    global f_num
    global math
    math= "add"
    f_num= int(first_number)
    e.delete(0, END)

def equal():
    second_number= e.get()
    e.delete(0,END)
    if (math== "add"):
        e.insert(0, f_num + int(second_number))
    if (math== "sub"):
        e.insert(0, f_num - int(second_number))
    if (math== "mul"):
        e.insert(0, f_num * int(second_number))
    if (math== "div"):
        e.insert(0, f_num / int(second_number))

def buttonMul():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(first_number)
    e.delete(0, END)

def buttonDiv():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)
def sub():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(first_number)
    e.delete(0, END)


myButton1 = Button(root, text="1",padx=40,pady=20,bg="blue", command= lambda :buttonClick(1))
myButton2 = Button(root, text="2",padx=40,pady=20,bg="red",command=lambda : buttonClick(2))
myButton3 = Button(root, text="3",padx=40,pady=20,bg="yellow",command=lambda : buttonClick(3))
myButton4 = Button(root, text="4",padx=40,pady=20,bg="green",command= lambda : buttonClick(4))
myButton5 = Button(root, text="5",padx=40,pady=20,command=lambda : buttonClick(5))
myButton6 = Button(root, text="6",padx=40,pady=20,command=lambda : buttonClick(6))
myButton7 = Button(root, text="7",padx=40,pady=20,command=lambda : buttonClick(7))
myButton8 = Button(root, text="8",padx=40,pady=20,command=lambda : buttonClick(8))
myButton9 = Button(root, text="9",padx=40,pady=20,command=lambda : buttonClick(9))
myButton0 = Button(root, text="0",padx=40,pady=20,command=lambda : buttonClick(0))
myButtonP = Button(root, text="+",padx=40,pady=20,command=add)
myButtonM = Button(root, text="-",padx=40,pady=20,command=lambda : sub)
myButtonC = Button(root, text="CLR",padx=36,pady=20, command= Clear)
myButtonE = Button(root, text="=",padx=40,pady=20,command=equal)
myButtont = Button(root, text="C",padx=40,pady=20,command=lambda : buttonClick())
myButton_m= Button(root, text="*",padx=40,pady=20,command=lambda : buttonMul())
myButtont_d = Button(root, text="/",padx=40,pady=20,command=lambda : buttonDiv())
myButtont_d = Button(root, text="/",padx=40,pady=20,command=lambda : buttonDiv())
myButtont_h = Button(root, text="HJ",padx=38,pady=20)


myButton1.grid(row=2, column=0)
myButton2.grid(row=2, column=1)
myButton3.grid(row=2, column=2)

myButton4.grid(row=3, column=0)
myButton5.grid(row=3, column=1)
myButton6.grid(row=3, column=2)

myButton7.grid(row=4, column=0)
myButton8.grid(row=4, column=1)
myButton9.grid(row=4, column=2)

myButton0.grid(row=5, column=0)
myButtonP.grid(row=5, column=1)
myButtonM.grid(row=5, column=2)

myButtonE.grid(row=6, column=1)
myButtont.grid(row=6, column=2)
myButtont_h.grid(row=6, column=0)

myButton_m.grid(row=7, column=1)
myButtont_d.grid(row=7, column=2)
myButtonC.grid(row=7, column=0)




root.mainloop()