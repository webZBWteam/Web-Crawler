import sys
sys.path.append('/Users/zhubowen/Desktop/Web-Crawler/zbw/code')
from crawler4 import crawler
brower=crawler('http://weibo.com')
brower.log_in()
nums=eval(input('输入爬取的页数：'))
sears=input('输入爬虫关键词，用"/"分割：').split('/')
brower.get_outcomes(nums,sears)


