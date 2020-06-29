import glob
'''s=input().split('、')
for i in s:
    print('乘风破浪的姐姐'+' '+i+'/',end='')'''

def get_txt_name():
    txts = glob.glob('/Users/zhubowen/Desktop/Web-Crawler/zbw/dataset/*.txt')#这里写路径，*3得到所有只有评论的txt文件
    return txts

txts=get_txt_name()
for txt in txts:
    print(txt)
