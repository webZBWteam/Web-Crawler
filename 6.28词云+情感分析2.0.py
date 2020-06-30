import wordcloud as wc
import jieba
import matplotlib.pyplot as plt
import imageio
from scipy.misc import imread
from snownlp import SnowNLP
import numpy as np
import glob
plt.rc('figure', figsize=(15, 15))



def get_txt_name():
    txts = glob.glob('/Users/zhubowen/Desktop/Web-Crawler/zbw/dataset/*3.txt')#这里写路径，*3得到所有只有评论的txt文件
    return txts


#读取微博正文内容
def read_weibo():
    file =open('C:/Users/haome/Desktop/demo2.txt',encoding='utf-8')
    all_text =''
    i=0
    while 1:
        context = file.readline()
        all_text = all_text + context
        if len(context) ==0:
            break
    file.close()
    print('succeed0')

#读取微博评论内容，避开ID
def read_pinglun():
    file =open('C:/Users/haome/Desktop/demo3.txt',encoding='utf-8',errors='ignore')
    all_text =''
    i=0
    while 1:
        context = file.readline()
        i=i+1
        if(i==4):
            all_text = all_text + context
            i=0
        if len(context) ==0:
            break
    file.close()
    print('succeed0')

#读取微博+评论文档，避开无关内容
file =open('C:/Users/haome/Desktop/demo1.txt',encoding='utf-8',errors='ignore')
i=0
all_text=''
context=file.readline()
while 1:
    if '-----微博正文-----' in context:
        i=1
        context=file.readline()
        all_text=all_text+context
        while 1:
            context=file.readline()
            if '-----微博正文-----' in context:
                break
            if len(context) ==0:
                break
            i=i+1
            if(i==4):
                all_text = all_text + context
                i=0
    if len(context) ==0:
        break
file.close()
print('succeed0')

#对每条内容进行情感分析
all_text=all_text.replace(' ','')
sentimentslist=[]
file.close()
for i in all_text:
    s=SnowNLP(i)
##    print(s.sentiments)
    sentimentslist.append(s.sentiments)
#情感分析绘制柱状图
plt.hist(sentimentslist,bins=np.arange(0,1,0.01),facecolor='b')
plt.xlabel('情绪指数')
plt.ylabel('分词数量')
plt.title('情感分析图')
plt.rcParams['font.sans-serif']=['SimHei']
plt.show()

#去除没有意义的虚词，虚词在unless文件中保存
excludes = open(file='C:/Users/haome/Desktop/unless.txt',encoding = 'utf-8').read().splitlines()
for i in excludes:
    all_text=all_text.replace(i,'')
all_text=all_text.replace(' ','')
print('succeed1')

#利用jieba库进行分词处理，某些人名需要作为新词加入词库
jieba.load_userdict('C:/Users/haome/Desktop/name.txt')
all_seg = jieba.cut(all_text, cut_all=False)
all_word =' '
for seg in all_seg:
    all_word = all_word +  seg + ' '
print('succeed2')

#利用worldcloud制造词云
font='C:/Windows/Fonts/simfang.ttf'
color_mask = imageio.imread("C:/Users/haome/Desktop/love.jpg")
cloud = wc.WordCloud( font_path=font,#设置字体  
                      background_color="white", #背景颜色  
                      max_words=200,# 词云显示的最大词数  
                      mask=color_mask,#设置背景图片  
                      max_font_size=150, #字体最大值  
                      mode="RGBA",
                      width=500,
                      height=400,
                      collocations=False)
# 绘制词云图
mywc = cloud.generate(all_word)
plt.imshow(mywc)
plt.axis("off")
plt.show()
print("succeed")
