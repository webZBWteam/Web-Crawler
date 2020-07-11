from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import urllib
import urllib.request
import requests
import glob
import time
import pymysql
from tkinter import *
import tkinter.messagebox
import PIL
from PIL import Image, ImageTk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        l1=Label(self,text='输入视频网址')
        l1.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        l2=Label(self,text='输入保存后的文件名')
        l2.pack()
        self.loc = Entry(self)
        self.loc.pack()
        self.alertButton = Button(self, text='下载', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'https://haokan.baidu.com/v?vid=15383225733972031503&pd=bjh&fr=bjhauthor&type=video'
        loc = self.loc.get() or '乘风破浪的姐姐'
        get_video(name,loc)
        root = Toplevel()
        root.title("success")
        la=tkinter.Label(root,text='success!!!!!!')
        la.pack()
        '''di_zhi = name + '.jpg'
        img_open = Image.open(di_zhi)
        size = 900, 900
        img_open.thumbnail(size)
        img_jpg = ImageTk.PhotoImage(img_open)
        label_img = Label(root, image=img_jpg)
        label_img.pack()'''
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
def error(brower):
    print('error!!!!!')
    brower.quit()
def get_video(name,loc):
    brower = webdriver.Safari()
    url=name
    #url = input('请输入你要下载视频的网站（目前只支持好看视频）：')
    #name = input('输入你希望保存的文件名：')
    try:
        brower.get(url)
    except:
        error(brower)
    time.sleep(2)
    try:
        download = brower.find_element_by_xpath('//video[@mediatype="video"]')
        download = download.get_attribute('src')
    except:
        error(brower)
    r = requests.get(download)
    with open(loc + '.mp4', 'wb') as fp:
        fp.write(r.content)
    brower.quit()

app = Application()
# 插入图片和背景的相关代码，必须与mainloop()放在相同的位置，否则不能显示，原因不详
photo = PhotoImage(file="bdb615b791926448aaa9b7ccd5c8329f.gif")
app.theLabel = Label(app,
                     text="网络视频下载（目前仅支持好看视频）",  # 内容
                     justify=LEFT,  # 对齐方式
                     image=photo,  # 加入图片
                     compound=CENTER,  # 关键:设置为背景图片
                     font=("华文行楷", 20),  # 字体和字号
                     fg="red")  # 前景色
app.theLabel.pack()
# 设置窗口标题:
app.master.title('视频下载小程序')
# 主消息循环:
app.mainloop()