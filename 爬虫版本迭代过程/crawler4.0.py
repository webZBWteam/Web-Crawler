from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class crawler:
    def __init__(self,url):#初始化crawler类，实现浏览器的初始化和网页的打开
        try:
            self.brower = webdriver.Safari()
            self.url = url
            self.brower.get(self.url)
            self.wait = self.waite(self.brower)
            self.wait = WebDriverWait(self.brower, 10)
            self.brower.maximize_window()
            time.sleep(5)
        except:
            self.error()
    def waite(self,brower):#设置显式等待，防止由于页面未成功夹在所出现对错误
        return WebDriverWait(brower,10)
    def error(self):#错误处理，输出错误信息，并将浏览器关闭
        self.brower.quit()
        print('error!!!!!')
    def quit(self):#完成爬虫任务，退出页面
        print('succeed!!!!!')
        self.brower.quit()
    def log_in(self):#登录微博账号，这里需要用户扫描二维码，并且根据提示确认扫描成功
        try:
            time.sleep(1)
            clic=self.wait.until(EC.presence_of_element_located(By.XPATH,'//a[@href="javascript:void(0)"]'))
            time.sleep(1)
            clic.click()
            time.sleep(1)
            clic = self.wait.until(EC.presence_of_element_located(By.XPATH, '//a[@action-data="tabname=qrcode"]'))
            clic.click()
            time.sleep(5)
            confirm=input('enter "yes" to confirm you have scan the code')
            if confirm=='yes':
                self.brower.refresh()
        except:
            self.error()
    def search(self,sear):#搜索关键词
        try:
            inp=self.wait.until(EC.presence_of_element_located(By.XPATH,'//input[@node-type="searchInput"]'))
            time.sleep(3)
            inp.send_keys(sear)
            time.sleep(1)
            clic=self.wait.until(EC.presence_of_element_located(By.XPATH,'//a[@node-type="searchSubmit"]'))
            time.sleep(1)
            clic.click()
        except:
            self.error()
    def open_comments(self):#打开所有评论
        try:
            time.sleep(3)
            clics = self.wait.until(EC.presence_of_all_elements_located(By.XPATH, '//a[@action-type="feed_list_comment"]'))
            for clic in clics:
                clic.send_keys(Keys.ENTER)
                time.sleep(1)
        except:
            print('no comment!!!')
    def open_weibo(self):#打开所有微博
        try:
            clics=self.wait.until(EC.presence_of_all_elements_located(By.XPATH,'//a[@action-type="fl_unfold"]'))
            for clic in clics:
                clic.send_keys(Keys.ENTER)
                time.sleep(1)
        except:
            print('no weibo to open!!!')
    def find_weibo(self):#找到所有微博的位置
        time.sleep(1)
        try:
            txts = self.wait.until(EC.presence_of_all_elements_located(By.XPATH, '//p[@node-type="feed_list_content"]'))
            return txts
        except:
            self.error()
    def find_comments_position(self):#找到所有评论的位置
        time.sleep(1)
        try:
            comments=self.wait.until(EC.presence_of_all_elements_located(By.XPATH,'//div[@class="card-together"]'))
            return comments
        except:
            self.error()
    def find_comments_detail(self):#找到所有评论的内容
        time.sleep(1)
        try:
            infos = self.wait.until(EC.presence_of_all_elements_located(By.XPATH, '//div[@class="txt"]'))
            return infos
        except:
            print('no comments!!!!!')
    def next_page(self):#实现翻页功能
        try:
            clic=self.wait.until(EC.presence_of_element_located(By.XPATH,'//a[@class="next"]'))
            clic.send_keys(Keys.ENTER)
        except:
            self.error()
    def get_outcomes(self,num):#获取微博数据和评论数据，保存为txt格式，其中num参数表示获取数据的页数
        file1 = open('demo1.txt', 'w')  # 微博和评论
        file2 = open('demo2.txt', 'w')  # 仅微博
        file3 = open('demo3.txt', 'w')  # 仅评论
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
                infos = self.find_comments_detail()
                for info in infos:
                    file1.writelines(info.text)
                    file3.writelines(info.text)
                    # print(info.text)
            self.next_page()