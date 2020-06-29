import glob
import re


def load_txt():  # 导入txt文件名
    try:
        txts = glob.glob('/Users/zhubowen/Desktop/Web-Crawler/zbw/dataset/*3.txt')
        return txts
    except:
        print('no such txt found!!!!!')


def read_txt(txt):  # 读取txt文件中的内容
    txt1 = open(txt)
    txt2 = open(txt)
    txt1.readline()
    names = []
    while True:
        content1 = txt1.readline()
        content2 = txt2.readline()
        #print(content1)
        #print(content2)
        if content1 == '                        ：\n':
            names.append(content2.lstrip()[0:-2])
        elif len(content1) == 0:
            return names


def db_load_data():  # 将数据导入数据库中
    txts = load_txt()
    for txt in txts:
        names = read_txt(txt)
        print(names)

db_load_data()
