from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import glob
import time
import pymysql
#import confirm

class crawler:
    def __init__(self,url):#初始化crawler类，实现浏览器的初始化和网页的打开
        try:
            self.brower = webdriver.Safari()
            self.url = url
            self.brower.get(self.url)
            self.wait = self.waite(self.brower)
            self.brower.maximize_window()
            time.sleep(10)
        except:
            self.web_error()
    def waite(self,brower):#设置显式等待，防止由于页面未成功夹在所出现对错误
        return WebDriverWait(brower,5)
    def web_error(self):#错误处理，输出错误信息，并将浏览器关闭
        self.brower.quit()
        print('error!!!!!')
    def database_error(self):#数据库错误处理
        self.conn.close()
        print('database error!!')
    def quit(self):#完成爬虫任务，退出页面
        print('succeed!!!!!')
        self.brower.quit()
    def log_in(self):#登录微博账号，这里需要用户扫描二维码，并且根据提示确认扫描成功
        try:
            time.sleep(1)
            clic = self.brower.find_element_by_xpath('//a[@href="javascript:void(0)"]')
            time.sleep(1)
            clic.click()
            time.sleep(1)
            clic = self.brower.find_element_by_xpath('//a[@action-data="tabname=qrcode"]')
            clic.click()
            time.sleep(30)
            #confirm.confi()
            #confirm=input('enter "yes" to confirm you have scan the code')
            #if confirm=='yes':
                #self.brower.refresh()
            #time.sleep(2)
            clic = self.brower.find_element_by_xpath('//a[@node-type="searchSubmit"]')
            clic.send_keys(Keys.ENTER)
        except:
            self.web_error()
    def search(self,sear):#搜索关键词
        time.sleep(2)
        try:
            inp = self.brower.find_element_by_xpath('//input[@node-type="text"]')
            time.sleep(2)
            inp.send_keys(sear)
            time.sleep(2)
            clic = self.brower.find_element_by_xpath('//button[@node-type="submit"]')
            time.sleep(2)
            clic.send_keys(Keys.ENTER)
        except:
            self.web_error()
    def open_comments(self):#打开所有评论
        try:
            time.sleep(3)
            clics = self.brower.find_elements_by_xpath('//a[@action-type="feed_list_comment"]')
            for clic in clics:
                clic.send_keys(Keys.ENTER)
                time.sleep(1)
        except:
            print('no comment!!!')
    def open_weibo(self):#打开所有微博
        try:
            clics = self.brower.find_elements_by_xpath('//a[@action-type="fl_unfold"]')
            for clic in clics:
                clic.send_keys(Keys.ENTER)
                time.sleep(1)
        except:
            print('no weibo to open!!!')
    def find_weibo(self):#找到所有微博的位置
        time.sleep(1)
        try:
            txts = self.brower.find_elements_by_xpath('//p[@node-type="feed_list_content"]')
            return txts
        except:
            self.web_error()
    def find_comments_position(self):#找到所有评论的位置
        time.sleep(1)
        try:
            comments = self.brower.find_elements_by_xpath('//div[@class="card-together"]')
            return comments
        except:
            self.web_error()
    def find_comments_detail(self,comment):#找到所有评论的内容
        time.sleep(1)
        try:
            infos = comment.find_elements_by_xpath('//div[@class="txt"]')
            return infos
        except:
            print('no comments!!!!!')
    def next_page(self):#实现翻页功能
        try:
            clic = self.brower.find_element_by_xpath('//a[@class="next"]')
            clic.send_keys(Keys.ENTER)
        except:
            self.web_error()
    def names(self,sear):#定义文件名
        name=[]
        for i in range(1,4):
            name.append(sear+str(i)+'.txt')
        return name
    def get_outcomes(self,num,sear):#获取微博数据和评论数据，保存为txt格式，其中num参数表示获取数据的页数
        self.search(sear)
        name = self.names(sear)
        file1 = open(name[0], 'w')  # 微博和评论
        file2 = open(name[1], 'w')  # 仅微博
        file3 = open(name[2], 'w')  # 仅评论
        for i in range(num):
            self.open_weibo()
            self.open_comments()
            txts = self.find_weibo()
            comments = self.find_comments_position()
            for txt, comment in zip(txts, comments):
                file1.writelines('-----微博正文-----')
                file1.writelines(txt.text)
                file2.writelines(txt.text)
                # print(txt.text)
                infos = self.find_comments_detail(comment)
                for info in infos:
                    file1.writelines(info.text)
                    file3.writelines(info.text)
                    # print(info.text)
            self.next_page()