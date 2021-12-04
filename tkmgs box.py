'''MESSAGE BOX'''

from tkinter import *
import tkinter.messagebox
root= Tk()

#tkinter.messagebox.showinfo("title","example")
#tkinter.messagebox.showwarning("alert","warning")
#tkinter.messagebox.showerror("error","error o0ccured")
#tkinter.messagebox.askquestion("ask","do you love me?")
tkinter.messagebox.askokcancel("confirm","ok?")

root.mainloop()