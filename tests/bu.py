def PageUse():
    msg.showinfo("사용방법", "띄워진 창 안에서\n노트를 작성하세요 ✍️")
def PageLicens():
    msg.showinfo("라이센스", "MIT License\n\nⓒ 2021 차한음 😎")
def PageVersion():
    msg.showinfo("버전", "현재 버전 v2.1.1 ✋")
def MenuHelp(root):
    menu = Menu(root)
    help = Menu(menu, tearoff=0)
    help.add_command(label="사용방법", command=PageUse)
    help.add_command(label="라이센스", command=PageLicens)
    help.add_command(label="버전", command=PageVersion)
    menu.add_cascade(label="도움말", menu=help)
    root.config(menu=menu)
