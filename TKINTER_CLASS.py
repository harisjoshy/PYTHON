from tkinter import *
root = Tk()

class demo:
    def __init__(self,root1):
        frame= Frame(root1)
        frame.pack()
        self.Print=Button(frame,text="hello",command=self.Print)
        self.Print.pack()
        Button(frame,text="exit",command= frame.quit).pack()

    def Print(self):
        print("helow world")

obj = demo(root)

root.mainloop()