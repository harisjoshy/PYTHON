'''
TKinter IS A GUI LIBRARY
'''

from tkinter import *
root = Tk()
#frame= Frame(root)
#def ButtonClick():
    #print("clicked")
Label(root,text="Haris",bg="red").grid(row=0,column=0)
Label(root,text="joshy",bg="red").grid(row=1,column=0)

Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1,column=1)








root.mainloop()