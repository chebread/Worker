# 급히 쓰는 노트
from tkinter import *
from tkinter import messagebox as msg
from clint.textui import *
import tkinter.font as tf

# main settings
root = Tk() # use to tkinter
root.title("Worker")
root.geometry("260x245")
#Help
def PageUse():
    msg.showinfo("사용방법", "띄워진 창 안에서\n노트를 작성하세요 ✍️")
def PageLicens():
    msg.showinfo("라이센스", "MIT License\n\nⓒ 2021 차한음 😎")
def PageVersion():
    msg.showinfo("버전", "현재 버전 v2.1.0 ✋")
def MenuHelp():
    global root
    menu = Menu(root)
    help = Menu(menu, tearoff=0)
    help.add_command(label="사용방법", command=PageUse)
    help.add_command(label="라이센스", command=PageLicens)
    help.add_command(label="버전", command=PageVersion)
    menu.add_cascade(label="도움말", menu=help)
    root.config(menu=menu)
# main Function
def Input():
    global root
    text = Text(root, selectforeground="blue violet",borderwidth=5,\
    tabs=23, font=15, fg="medium spring green", bg="medium purple",\
    highlightbackground="medium purple", highlightthickness=0)
    text.pack(fill="both", expand=True)
    text.configure(font=tf.Font(weight="bold"))
def Play():
    Input()
    MenuHelp()
# codes
Play()
root.mainloop()