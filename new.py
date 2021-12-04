from tkinter import *

def fun():
    print("clicked")
root = Tk()
root.geometry("100x200")
menu= Menu(root)

root.config(menu=menu)

subMenu = Menu(menu)

menu.add_cascade(Label="file",menu=subMenu)
subMenu.add_command(Label="save",command=fun)
subMenu.add_command(Label="exit",command=fun)


root.mainloop()