import jieba
import os
import re
import collections
import numpy as np
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#import docx
file = open("/Users/reallaggywang/Desktop/demo1.txt")
n=1
#为词库增加关键词
jieba.add_word('乘风破浪的姐姐')
jieba.add_word('李斯丹妮')
jieba.add_word('张雨绮')
jieba.add_word('白冰')
jieba.add_word('陈松伶')
jieba.add_word('丁当')
jieba.add_word('黄圣依')
jieba.add_word('黄龄')
jieba.add_word('海陆')
jieba.add_word('金晨')
jieba.add_word('金莎')
jieba.add_word('蓝盈莹')
jieba.add_word('刘芸')
jieba.add_word('孟佳')
jieba.add_word('宁静')
jieba.add_word('吴昕')
jieba.add_word('沈梦辰')
jieba.add_word('王丽坤')
jieba.add_word('王霏霏')
jieba.add_word('王智')
jieba.add_word('万茜')
jieba.add_word('许飞')
jieba.add_word('郁可唯')
jieba.add_word('伊能静')
jieba.add_word('袁咏琳')
jieba.add_word('张含韵')
jieba.add_word('张萌')
jieba.add_word('钟丽缇')
jieba.add_word('郑希怡')
jieba.add_word('朱婧汐')
jieba.add_word('黄晓明')
jieba.add_word('杜华')
words=[]
while 1:
    line=file.readline()#读取每一行
    if not line:
        break;
    list=jieba.cut(line,cut_all=False)
    print("第%d条微博的分词结果："%(n))
    print(" ".join(list)+"\n")
    n=n+1
    pass
#开始画词云图
file.close()
CURDIR = os.path.abspath(r"/Users/reallaggywang/Desktop")
TEXT = os.path.join(CURDIR,  'demo1.txt')
PICTURE= os.path.join(CURDIR,  '3.jpg')
FONT = os.path.join(CURDIR, 'Songti.ttc')
file2 = open("/Users/reallaggywang/Desktop/demo1.txt")
line2=file2.read()
list2=jieba.cut(line2,cut_all=False)#切词
words=collections.Counter(list2)#统计词频
file2.close()
background = np.array(Image.open(PICTURE))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white",
                   mask=background,
                   stopwords=stopwords,
                   font_path=FONT,
                   max_words=400,
                   max_font_size=80,
                   scale=64
               )
wc.generate_from_frequencies(words)
wc.to_file('sister.jpg')
plt.imshow(wc)