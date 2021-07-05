# 급히 쓰는 노트
from tkinter import *
from tkinter import messagebox as msg
from clint.textui import *
import tkinter.font as tf

root = Tk() # use to tkinter
root.title("Worker")
root.geometry("240x220") # 가로x세로

def PageUse():
    msg.showinfo("사용방법", "띄워진 창 안에서\n노트를 작성하세요 ✍️")
def PageLicens():
    msg.showinfo("라이센스", "MIT License\n\nⓒ 2021 차한음 😎")
def PageVersion():
    msg.showinfo("버전", "현재 버전 v2.1.1 ✋")
def Menus():
    menu = Menu(root)
    help = Menu(menu, tearoff=0)
    help.add_command(label="사용방법", command=PageUse)
    help.add_command(label="라이센스", command=PageLicens)
    help.add_command(label="버전", command=PageVersion)
    menu.add_cascade(label="도움말", menu=help)
    root.config(menu=menu)
def Input():
    t = Text(root, selectforeground="white",borderwidth=5,\
    tabs=24, font=17, fg="black", bg="light sky blue",\
    highlightbackground="medium purple", highlightthickness=0)
    t.pack(fill="both", expand=True)
    t.configure(font=tf.Font(family="Apple SD 산돌고딕 Ne", weight="bold"))
def Play():
    Input()
    Menus()
    
Play()
root.mainloop()