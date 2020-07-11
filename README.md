

# '乘风破浪的姐姐'项目介绍
![image-process](https://img.shields.io/badge/python-3.7-green.svg)
![image-process](https://img.shields.io/badge/pycharm-2020.1.2-orange)
![image-process](https://img.shields.io/badge/PIL-1.1.6-red)
![image-process](https://img.shields.io/badge/tkinter-1.1.0-yellow)
![image-process](https://img.shields.io/badge/wordcloud-1.7.0-green)
![image-process](https://img.shields.io/badge/selenium-3.141.0-orange)

![image-process](https://img.shields.io/badge/mysql-8.0.19-lightgrey)
![image-process](https://img.shields.io/badge/Dreaweaver-20.0-blue)
![image-process](https://img.shields.io/badge/Echarts-3.0-orange)
![image-process](https://img.shields.io/badge/html-5-red)

![image-process](https://img.shields.io/badge/Bootstrap-%E7%BD%91%E9%A1%B5%E5%B8%83%E5%B1%80-yellow)
![image-process](https://img.shields.io/badge/Content--Type-%E7%BD%91%E9%A1%B5%E6%B8%B2%E6%9F%93-brightgreen)
![image-process](https://img.shields.io/badge/keywords-%E6%A0%87%E7%AD%BE-blue)
![image-process](https://img.shields.io/badge/masonry-%E7%80%91%E5%B8%83%E5%9E%8B%E5%9B%BE%E7%89%87%E5%B8%83%E5%B1%80-orange)
![image-process](https://img.shields.io/badge/fadeInUp-%E5%8A%A8%E6%80%81%E5%B8%83%E5%B1%80-green)
![image-process](https://img.shields.io/badge/element-%E5%A4%9A%E9%87%8D%E5%B8%83%E5%B1%80-lightgrey)
![image-process](https://img.shields.io/badge/marquee-%E5%9B%BE%E7%89%87%E6%94%BE%E7%BD%AE%E5%A4%9A%E6%A0%B7%E5%8C%96-red)
![image-process](https://img.shields.io/badge/%E8%87%AA%E5%AE%9A%E4%B9%89-p%E3%80%81img%E3%80%81a%E6%A0%87%E7%AD%BE-lightgrey)

![image-process](https://img.shields.io/badge/bootstrap.min-css-red)
![image-process](https://img.shields.io/badge/jQuery.lightninBox-css-yellow)
![image-process](https://img.shields.io/badge/style--core-css-blue)
![image-process](https://img.shields.io/badge/echarts.min-js-red)
![image-process](https://img.shields.io/badge/jquery.isotope.min-js-green)
![image-process](https://img.shields.io/badge/jquery-js-brightgreen)

目录
=================

   * ['乘风破浪的姐姐'项目介绍](#乘风破浪的姐姐项目介绍)
   
        * [1. 项目概要](#1-项目概要)
         
        * [2. 项目进度](#2-项目进度)
         
        * [3. 实现目标](#3-实现目标)
         
        * [4. 数据来源](#4-数据来源)
         
        * [5. 技术路线](#5-技术路线)
         
        * [6. 项目亮点](#6-项目亮点)
         
        * [7. API接口介绍](#7-api接口介绍)
         
         
### 1. 项目概要

此项目旨在实现《乘风破浪的姐姐》微博数据获取，并通过网页手段展示，主页（总览页）展示乘风破浪的姐姐的总体情况以及小组成员，并且可以根据需求到综艺详情页、pick页（姐姐分类索引）、姐姐个人详情页。对代码进行了较高程度的抽象和封装，提供API方便直接调用，并给出两个代码示例化的思路。

### 2. 项目进度

![image-process](https://s1.ax1x.com/2020/07/11/UluHAK.jpg)

### 3. 实现目标
> * crawler类和cloud类高度抽象封装，并给出调用接口和说明文档
> * '实时词云'生成&'好看视频'下载器两个实例窗口小程序
> * 对爬取数据中的有效内容进行提取
> * 词云的获取与可视化，图片形状和字体随机；对每条内容进行情感分析，获得柱状图
> * 数据库连接和使用
> * 美观有效的数据呈现


### 4. 数据来源

> * 图片：微博、程序生成、百度
> * 视频：好看视频
> * 文字：微博、百度


### 5. 技术路线
1.数据获取
使用Web自动化测试工具selenium进行数据获取，攻克反爬难关；
使用requests和beautiful soap库对于反爬技术弱的网站进行数据获取，提高效率；
对不同的网站定制爬虫策略，实现数据精准化获取；
对爬虫程序进行高程度封装，方便其他人调用。

2.数据处理
使用snownlp、jieba、load_userdict、replace、wordcloud、imageio、pymysql等功能对数据进行处理；
对大部分复用性比较高的代码进行封装，方便后续的使用；

3.数据呈现（网页）
使用js、css等语言，结合案例、教程，实现大致网页框架；
使用viewport响应式设计；
使用"Content-Type"等功能实现网页渲染环境；
使用keywords标签，易于用户检索本网站；
使用bootstrap实现网页布局，保证元素随网页大小变动而合理变化，美化界面；
学习marquee等多种方法实现图片放置多样化；
使用audio标签实现背景音乐控件；
使用id标签实现定位功能；
自定义cursor，制作cur文件，实现自定义鼠标，通过学习制作鼠标点击动画；
自定义video、hover等css功能，对jquery、bootstrap、layer等库进行比较取舍，实现视频弹窗播放、画中画功能；
自定义p、img、a等标签，实现个性化网页；
实现网页中图片的景深效果；
利用代码搭构一个仓库数组，将爬虫获取的数据输出的数据以及网络的部分内容定好输入后，即可获得该小姐姐的个人详细网页代码

4.可扩展性
结合tkinter库和我们封装的crawler类和cloud类给出“微博实时词云生成”和“好看视频下载器”两个实例化窗口界面程序，展示了封装的有效性和程序的可扩展性

### 6. 项目亮点

1.使用Web自动化测试工具selenium进行数据获取，模拟人对网页的操作，减少被系统反爬机制识别的可能，但在效率上做出了一些牺牲。

2.对爬虫的方法进行了比较详细的封装（封装成了crawler类），并给出相应的API接口；将步骤尽可能细分，使函数有更多重组和使用的可能性，方便其他人对函数进行自己的拼接和调用，使用更加方便简洁（事实上实际上调用的函数只有十几行，极大地减小了编程的负担）。同时，给出窗口应用“微博实时词云”，展示crawler类在本项目之外的其他可能，也为使用者对crawler类的创新性应用提供了一个简单的思路。

3.针对网页展示中对视频信息的获取需求，给出窗口应用“视频下载”（目前只支持从“好看视频”网上下载视频），扩展了项目程序的使用范围，增强代码的实用性。

4.利用数据库主键的特点筛选用户，从而不重不漏获取用户信息。

5.注重程序的可移植性和可扩展性，大部分爬虫程序都给出对应的用户输入接口，使程序不拘泥于一个应用，一般来说我们的程序可以实现对应功能任意关键词的搜索和数据获取。

6.巧妙的反爬策略：使用selenium库、多次重启浏览器、使用二维码登录从而绕过验证码（或验证程序）环节等等

7.爬虫讲究效率，虽然selenium库能够模拟人的操作，也能加载完整页面的内容，但是效率低下，即使打开多线程也无法提高速度（受限于网速），在设计的过程中我们秉持着能不用selenium库就不用的原则，尽可能地提高爬虫效率

8.注重用户体验，给出remove功能，及时删除使用过的数据，不占用系统过多的内存

9.网页设计美观大方，功能全面，同时考虑到诸多用户操作的因素，实现了对用户友好的特点，数据呈现简明有效。

### 7. API接口介绍

**一、爬虫框架**

爬虫框架有多个对外接口。如果您希望获取微博数据，欢迎将不同方法有效组合，以获得最佳效果！

**A.说明对象**

crawler5的crawler类。

**B.类变量**
> * self.brower: 初始化浏览器，支持Safari。
> * self.url:获取url地址，默认参数为'http://weibo.com'。
> * self.wait: 设定显示等待机制，防止因网页为加在完成而出现错误。
> * self.conn: 接受两个字符串参数password和db。
> * self.cursor: 数据库游标。

**C.类方法**
1.	__ init __(self,url='http://weibo.com') 
初始化爬虫对象。其中url为目标网站链接，类型为字符串，默认值为 'http://weibo.com'。
2.	waite(self,brower) 设置显式等待，防止由于页面未成功夹在所出现对错误。其中brower为webdriver对象。
3.	web_error(self) 爬虫错误处理。
4.	database_error(self)数据库错误处理。
5.	quit(self)退出浏览器。
6.	log_in(self)登录微博账号，这里需要用户扫描二维码，并且根据提示确认扫描成功。
7.	search(self,sear) 搜索关键词，其中sear为搜索关键词。类型为字符串。
8.	open_comments(self) 打开所有评论
9.	open_weibo(self) 打开所有微博（有些微博存在阅读全文链接，需要将其打开才能获取所有的数据）
10.	find_weibo(self) 找到所有微博的位置，返回存储代表微博位置的selenium迭代对象
11.	find_comments_position(self) 找到所有评论的位置，返回存储代表评论位置的selenium迭代对象
12.	find_comments_detail(self,comment)找到所有评论的内容，输入的参数是代表评论位置的一个selenium对象，返回存储代表评论位置的selenium迭代对象
13.	next_page(self)实现翻页功能
14.	names(self,sear)定义文件名，输入的参数是一个字符串，具体的内容为用户的搜索关键词，返回存有文件名的列表
15.	get_outcomes(self,num,sears)获取微博数据和评论数据，保存为txt格式，其中num参数表示获取数据的页数，sears为列表类型，其中每一个元素为用户输入的搜索关键词
16.	database_link(self,password,db)连接数据库，输入的两个参数password和db分别是密码和数据库名称，为字符串类型
17.	load_txt(self)获取txt文件名，返回保存着所有txt文件名的一个列表
18.	read_txt(self,txt)读取txt文件中的内容，并将用户名提取出来
19.	db_insert_id(self,names)将用户名称插入数据库中，输入的参数是保存了用户名的列表
20.	db_load_user_id(self)将用户id数据导入数据库中
21.	find_user(self)搜索用户个人信息，返回用户信息的位置
22.	db_get_user_id(self)从数据库中获取用户信息，返回存有所有用户信息的列表
23.	db_load_user_info(self)向数据库中导入用户信息
24.	read_txt_comments(ttxt,comments, file)读取txt文件中的内容
25.	get_fcomments(self)得到规定格式的txt文件，针对评论
26.	remove(self,format)获取特定格式的文件名，其中format为文件的类型，是一个字符串类型的变量。
27.	delete(self,forms=['txt'])删除多余的文件，其中format为需要删除文件的类型，是一个列表类型的变量（可能有多个）,默认值为['txt']。

**二、获得词云和情感分析框架**

词云和情感分析框架含有对外接口，如果您希望根据文本内容生成词云或进行情感分，可以进行连接，以获得结果。

**A.说明对象**

 Cloud中的cloud类
 
**B.类变量**
> * self.dl_name：获取文件名字
> * self.name：获取文件地址
> * self.all_text：读取文件内容

**C.类方法**
1.	__ init __(self,name):初始化对象，其中name为文件名字，类型是字符串
2.	read_weibo(self): 读取微博正文内容
3.	read_pinglun(self): 读取微博评论内容，避开ID
4.	read_all(self): 读取微博+评论文档，避开无关内容
5.	mood(self): 对每条内容进行情感分析，最终生成图片并保存到本机
6.	ciyun(self): 词云的生成与数据的处理，最终生成柱状图并保存到本机

------

谢谢老师和助教哥哥姐姐的悉心指导和技术支持!
