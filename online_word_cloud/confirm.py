from tkinter import *

def quit(root):
    root.destroy()


def confi():
    root = Tk()
    root.title("微博登录")
    frame = Frame(root)
    frame.pack()
    theLabel = Label(root,
                     text='close the window to confirm you have scan the code!!',#内容
                     justify=LEFT,#对齐方式
                     font=("华文行楷",20),#字体和字号
                     fg = "red")#前景色
    theLabel.pack()
    root.mainloop()