import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
url="https://s.weibo.com/weibo?q=%E8%82%96%E6%88%98&topnav=1&wvr=6&Refer=top_summary"
headers = {'onnection': 'close','Content-Type':'text/html; charset=utf-8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36' }
data = requests.get(url, headers=headers).text
soup = BeautifulSoup(data, 'html.parser')
list1 = soup.find_all('p')
for i in list1:
    print(i.get_text())