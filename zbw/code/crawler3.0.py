from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

brower=webdriver.Safari()
url='https://weibo.com'
brower.get(url)
time.sleep(10)
wait = WebDriverWait(brower, 10)
brower.maximize_window()
try:
    time.sleep(1)
    clic = brower.find_element_by_xpath('//a[@href="javascript:void(0)"]')
    time.sleep(1)
    clic.click()
except:
    brower.quit()
    print('error')
try:
    time.sleep(1)
    clic = brower.find_element_by_xpath('//a[@action-data="tabname=qrcode"]')
    clic.click()
except:
    brower.quit()
    print('error')
try:
    time.sleep(5)
    s=input('enter yes to confirm you have scan the code')
    if s!='':
        brower.refresh()
    inp = brower.find_element_by_xpath('//input[@node-type="searchInput"]')
    time.sleep(3)
    inp.send_keys('乘风破浪的姐姐')
except:
    brower.quit()
    print('error')
try:
    time.sleep(1)
    clic = brower.find_element_by_xpath('//a[@node-type="searchSubmit"]')
    time.sleep(1)
    clic.click()
except:
    brower.quit()
    print('error')
file1=open('demo1.txt','w')#微博和评论
file2=open('demo2.txt','w')#仅微博
file3=open('demo3.txt','w')#仅评论
for i in range(20):
    try:
        time.sleep(3)
        clics = brower.find_elements_by_xpath('//a[@action-type="feed_list_comment"]')
        for clic in clics:
            clic.send_keys(Keys.ENTER)
            time.sleep(1)
        clics = brower.find_elements_by_xpath('//a[@action-type="fl_unfold"]')
        for clic in clics:
            clic.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(1)
        txts = brower.find_elements_by_xpath('//p[@node-type="feed_list_content"]')
        time.sleep(1)
        comments = brower.find_elements_by_xpath('//div[@class="card-together"]')
        time.sleep(1)
        for txt, comment in zip(txts, comments):
            file1.writelines('-----微博正文-----')
            file1.writelines(txt.text)
            file2.writelines(txt.text)
            #print(txt.text)
            try:
                infos = comment.find_elements_by_xpath('//div[@class="txt"]')
                for info in infos:
                    file1.writelines(info.text)
                    file3.writelines(info.text)
                    #print(info.text)
            except:
                file1.writelines('no comment!')
                file3.writelines('no comment!')
        try:
            clic = brower.find_element_by_xpath('//a[@class="next"]')
            clic.send_keys(Keys.ENTER)
        except:
            brower.quit()
    except:
        brower.quit()
        print('error')
brower.quit()


