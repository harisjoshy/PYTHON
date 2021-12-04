
'''self adjacent WIDGET'''

from tkinter import *
root = Tk()
Label(root,text="x direction", bg="cyan").pack(fill=X)

Label(root,text="y direction",bg="red").pack(side=LEFT,fill=Y)
Label(root,text="y direction",bg="red").pack(side=RIGHT,fill=Y)


root.mainloop()