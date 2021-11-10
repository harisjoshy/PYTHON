from tkinter import *
import pymysql

x = pymysql.connect(host='localhost',user='root', password='123456789@H',database='haris')
cr= x.cursor()

t= Tk()
t.geometry("500x500")
Label(text="name").place(x=10,y=10)
m= Entry()
m.place(x=55,y=12)

Label(text="age").place(x=10,y=35)
k= Entry()
k.place(x=55,y=37)


def submit2():
    n= m.get()
    s= k.get()
    cr.execute('insert into submit values(%s,%s)',(n,s))

    x.commit()
    x.close()
    t.mainloop()
    
    

Button(text="submit", command=submit2).place(x=40,y=65)
Label(text="UPDATE",fg="red",font=("times new roman",24,"bold")).place(x=0,y=85)

Label(text="Enter Name",fg="blue").place(x=5,y=120)
y= Entry()
y.place(x=70,y=120)


Label(text="Enter Age",fg="blue").place(x=5,y=150)
z= Entry()
z.place(x=70,y=150)



def update():
    v= y.get()
    i= z.get()
  
    cursor= x.cursor()
    cursor.execute(("update submit set age=%s where entry=%s"), (i,v))
    cursor.close()

    x.commit()
    x.close()
    t.destroy()
    t.mainloop()

Button(text="Update",fg="green",command=update).place(x=50,y=200)

t.mainloop()
