from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class crawler:
    def __int__(self,url):
        self.brower=webdriver.Safari()
        self.brower.get(url)
        self.wait = WebDriverWait(self.brower, 10)
    def error(self):
        self.brower.quit()
        print('ERROR!!!!!')
    def sleep(self):
        time.sleep(1)
    def enter_user_name(self,user_name):
        try:
            self.sleep()
            input = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
            self.sleep()
            input.send_keys(user_name)
        except:
            self.error()
    def enter_password(self,password):
        try:
            self.sleep()
            input = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
            input.send_keys(password)
        except:
            self.error()
    def submit_log(self):
        try:
            self.sleep()
            clic = self.wait.until(EC.presence_of_element_located((By.ID, 'loginAction')))
            self.sleep()
            clic.click()
        except:
            self.error()
    def log_in(self,user_name,password):
        self.enter_user_name(user_name)
        self.enter_user_name(password)
        self.submit_log()















