import requests
import json
import time
from lxml import html
etree = html.etree
import html
import re
from bs4 import BeautifulSoup


class Weibospider:
    def __init__(self):
        # 获取首页的相关信息：
        self.start_url = 'https://weibo.com/u/5644764907?page=1&is_all=1'

        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "max-age=0",
            "cookie": "_T_WM=54266336139; WEIBOCN_FROM=1110006030; XSRF-TOKEN=c46c3a; "
                      "SUB=_2A25z9wd-DeRhGeBO61oZ9SbOyTWIHXVRG6k2rDV6PUJbkdAKLWfDkW1NSlL97zD7g2MkpYdnbRbqJb9jSCf3gXDf; "
                      "SUHB=0oUodFAFYYDA12; SCF=AmT__xScJEKAUJVLqYsnJdZMpnsoTPX4dWfwRusM9kX2OnB-kIAFe-sVzB7eIaeenyCaA5w8Vvt-p5LLa_d5-Vo.; "
                      "SSOLoginState=1593014062; MLOGIN=1; M_WEIBOCN_PARAMS=lfid%3D1005052803301701%26luicode%3D20000174%26uicode%3D20000174",
            "referer": "https://www.weibo.com/u/5644764907?topnav=1&wvr=6&topsug=1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
        }
        self.proxy = {
            'HTTP': 'HTTP://180.125.70.78:9999',
            'HTTP': 'HTTP://117.90.4.230:9999',
            'HTTP': 'HTTP://111.77.196.229:9999',
            'HTTP': 'HTTP://111.177.183.57:9999',
            'HTTP': 'HTTP://123.55.98.146:9999',
        }

    def parse_home_url(self, url):  # 处理解析首页面的详细信息（不包括两个通过ajax获取到的页面）
        res = requests.get(url, headers=self.headers)
        response = res.content.decode().replace("\\", "")
        # every_url = re.compile('target="_blank" href="(/\d+/\w+\?from=\w+&wvr=6&mod=weibotime)" rel="external nofollow" ', re.S).findall(response)
        every_id = re.compile('name=(\d+)', re.S).findall(response)  # 获取次级页面需要的id
        home_url = []
        for id in every_id:
            base_url = 'https://weibo.com/aj/v6/comment/big?ajwvr=6&id={}&from=singleWeiBo'
            url = base_url.format(id)
            home_url.append(url)
        return home_url

    def parse_comment_info(self, url):  # 爬取直接发表评论的人的相关信息(name,info,time,info_url)
        res = requests.get(url, headers=self.headers)
        response = res.json()
        count = response['data']['count']
        html = etree.HTML(response['data']['html'])
        name = html.xpath("//div[@class='list_li S_line1 clearfix']/div[@class='WB_face W_fl']/a/img/@alt")  # 评论人的姓名
        info = html.xpath("//div[@node-type='replywrap']/div[@class='WB_text']/text()")  # 评论信息
        info = "".join(info).replace(" ", "").split("\n")
        info.pop(0)
        comment_time = html.xpath("//div[@class='WB_from S_txt2']/text()")  # 评论时间
        name_url = html.xpath("//div[@class='WB_face W_fl']/a/@href")  # 评论人的url
        name_url = ["https:" + i for i in name_url]
        comment_info_list = []
        for i in range(len(name)):
            item = {}
            item["name"] = name[i]  # 存储评论人的网名
            item["comment_info"] = info[i]  # 存储评论的信息
            item["comment_time"] = comment_time[i]  # 存储评论时间
            item["comment_url"] = name_url[i]  # 存储评论人的相关主页
            comment_info_list.append(item)
        return count, comment_info_list

    def write_file(self, path_name, content_list):
        for content in content_list:
            with open(path_name, "a", encoding="UTF-8") as f:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):
        start_url = 'https://weibo.com/u/5644764907?page={}&is_all=1'
        start_ajax_url1 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100406&is_all=1&page={0}&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1004065644764907&script_uri=/u/5644764907&pre_page={0}'
        start_ajax_url2 = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100406&is_all=1&page={0}&pagebar=1&pl_name=Pl_Official_MyProfileFeed__20&id=1004065644764907&script_uri=/u/5644764907&pre_page={0}'
        for i in range(12):  # 微博共有12页
            home_url = self.parse_home_url(start_url.format(i + 1))  # 获取每一页的微博
            ajax_url1 = self.parse_home_url(start_ajax_url1.format(i + 1))  # ajax加载页面的微博
            ajax_url2 = self.parse_home_url(start_ajax_url2.format(i + 1))  # ajax第二页加载页面的微博
            all_url = home_url + ajax_url1 + ajax_url2
            for j in range(len(all_url)):
                print(all_url[j])
                path_name = "第{}条微博相关评论.txt".format(i * 45 + j + 1)
                all_count, comment_info_list = self.parse_comment_info(all_url[j])
                self.write_file(path_name, comment_info_list)
                for num in range(1, 10000):
                    if num * 15 < int(all_count) + 15:
                        comment_url = all_url[j] + "&page={}".format(num + 1)
                        print(comment_url)
                        try:
                            count, comment_info_list = self.parse_comment_info(comment_url)
                            self.write_file(path_name, comment_info_list)
                        except Exception as e:
                            print("Error:", e)
                            time.sleep(60)
                            count, comment_info_list = self.parse_comment_info(comment_url)
                            self.write_file(path_name, comment_info_list)
                        del count
                        time.sleep(0.2)

                print("第{}微博信息获取完成！".format(i * 45 + j + 1))


if __name__ == '__main__':
    weibo = Weibospider()
    weibo.run()
