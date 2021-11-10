from tkinter import *
import pymysql

x = pymysql.connect(host="localhost",user="root",password="123456789@H",database="haris")
cr = x.cursor()
t = Tk()
t.geometry("800x500")
Label(text="Name",bg="green",fg="blue").place(x=10,y=10)

nm= Entry()
nm.place(x=55,y=10)

Label(text="Age",bg="cyan",fg="violet").place(x=10,y=35)
ag = Entry()
ag.place(x=55,y=35)

def abcd():
    import pymysql
    x = pymysql.connect(host="localhost",user="root",password="123456789@H",database="haris")
    cr = x.cursor()
    n=nm.get()
    d=ag.get()
    cr.execute("insert into submit values(%s,%s)",(n,d))
    x.commit()
    
    
  

s = Button(text="Submit",bg="yellow",command=abcd)
s.place(x=40,y=65)

Label(text="UPDATE",fg="red",font=("times new roman",24,"bold")).place(x=0,y=85)

Label(text="Enter Name",fg="blue").place(x=5,y=120)
y= Entry()
y.place(x=70,y=120)


Label(text="Enter Age",fg="blue").place(x=5,y=150)
k= Entry()
k.place(x=70,y=150)

def update():
    import pymysql
    x = pymysql.connect(host="localhost",user="root",password="123456789@H",database="haris")
    cr = x.cursor()
    r = y.get()
    q= k.get()
    cr.execute("update submit set age=%s where entry=%s",(r,k))
    x.commit()
    
    

Button(text="Update",fg="green",command=update).place(x=50,y=200)

s= Scrollbar()

s.pack(side=RIGHT,fill=Y)
tx= Text(height=10,width=20,yscrollcommand=s.set)
tx.place(x=480,y=50)
s.config(command=tx.yview)
tx.insert(INSERT,"CLICK TO SEE AVAILABLE DATA")


def view():
    import pymysql
    x = pymysql.connect(host="localhost",user="root",password="123456789@H",database="haris")
    cr = x.cursor()
    cr.execute("select * from submit")
    z = cr.fetchall()
    tx.delete("1.0",END)
    tx.insert(INSERT,"LOOK ITS THE DATA \n")
    hj= [','.join(map(str,l))for l in z]
  
    for i in hj:
        tx.insert(INSERT,'%s\n\n'%i)
    

b=Button(text="View Data",fg="green",command=view)
b.place(x=500,y=220)
x.close()
t.mainloop()




    
