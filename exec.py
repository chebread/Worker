# 급히 쓰는 노트
from typing import TextIO
from clint.textui import *
from tkinter import *

root = Tk() # use to tkinter
root.title("Worker")
root.geometry("260x245")
#root.configure(bg='black')
def Input(root):
    Text(root, fg="green", bg="purple", highlightbackground="purple").pack(fill="both", expand=True)
def Play(root):
    Input(root)

Play(root)
root.mainloop()