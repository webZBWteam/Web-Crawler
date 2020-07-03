from tkinter import *
import tkinter.messagebox
import PIL
from PIL import Image, ImageTk
name=''
loc=''
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()     
        self.createWidgets()
        
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.loc=Entry(self)
        self.loc.pack()
        self.alertButton = Button(self, text='搜索', command=self.hello)
        self.alertButton.pack()
 
    def hello(self):
        name = self.nameInput.get() or '乘风破浪的姐姐'
        loc=self.loc.get() or '乘风破浪的姐姐'
        online(name)
        root = Toplevel()
        root.title("词云展示")
        di_zhi = name + '.jpg'
        img_open = Image.open(di_zhi)
        size=900,900
        img_open.thumbnail(size)
        img_jpg = ImageTk.PhotoImage(img_open)
        label_img = Label(root, image=img_jpg)
        label_img.pack()
        root.mainloop()
        '''file_name='乘风破浪的姐姐'+name
        a=data(file_name)
        if '1' in file_name:
            a.read_all()
        elif '2' in file_name:
            a.read_weibo()
        elif '3' in file_name:
            a.read_pinglun()
        a.ciyun()'''
app = Application()
#插入图片和背景的相关代码，必须与mainloop()放在相同的位置，否则不能显示，原因不详
photo = PhotoImage(file="bdb615b791926448aaa9b7ccd5c8329f.gif")
app.theLabel = Label(app,
                     text="微博实时词云",#内容
                     justify=LEFT,#对齐方式
                     image=photo,#加入图片
                     compound = CENTER,#关键:设置为背景图片
                     font=("华文行楷",20),#字体和字号
                     fg = "red")#前景色
app.theLabel.pack()
# 设置窗口标题:
app.master.title('词云展示')
# 主消息循环:
app.mainloop()
