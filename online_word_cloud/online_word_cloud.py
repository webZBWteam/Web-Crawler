import sys
sys.path.append('/Users/zhubowen/Desktop/Web-Crawler/online_word_cloud')
from crawler5 import crawler
from DATA import data

brower=crawler('http://weibo.com')
brower.log_in()
nums=eval(input('输入爬取的页数：'))
sears=input('输入爬虫关键词：').split('/')
brower.get_outcomes(nums,sears)