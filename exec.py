# 급히 쓰는 노트
from tkinter import *
from clint.textui import *

root = Tk() # use to tkinter
root.title("Worker")
root.geometry("260x245")
#root.configure(bg='black')
def Input(root):
    Text(root, font=13, fg="medium spring green", bg="medium purple", highlightbackground="medium purple").pack(fill="both", expand=True)
def Play(root):
    Input(root)

Play(root)
root.mainloop()