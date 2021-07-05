from tkinter import *

root = Tk()
root.geometry("300x200")

def Read():
    print(textEx.get("1.0","end"))

textEx = Text(root, height=10)
textEx.pack()
btn = Button(root, height=1, width=10, text="R", command=Read)

btn.pack()

root.mainloop()


def Copy():
    global root
    root.clipboard_append(t)
def MenuEdit(root):
    menu = Menu(root)
    edit = Menu(menu, tearoff=0)
    edit.add_command(label="복사", command=Copy)
    edit.add_cascade(label="편집")
    root.config(menu=menu)
