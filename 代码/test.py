import jieba
#import pkuseg
file = open("/Users/reallaggywang/Desktop/demo1.txt")
n=1;
while 1:
    line=file.readline()
    if not line:
        break;
    list=jieba.cut(line,cut_all=False)
    print("第%d条微博的分词结果："%(n))
    print(" ".join(list)+"\n")
    n=n+1
    pass
file.close()
