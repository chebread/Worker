from tkinter import *

root = Tk()
root.title("hello")
root.geometry("300x200")

menu = Menu(root)

def Cmd():
    print("cmd")
menu_color = Menu(menu, tearoff=0)
menu_color.add_command(label="보라색", command=Cmd)
menu.add_cascade(label="색상", menu=menu_color)
root.config(menu=menu)
root.mainloop()