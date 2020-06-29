from DATA import data

file_name=input('请输入文件名:')
a=data(file_name)
if '1' in file_name:
    a.read_all()
elif '2' in file_name:
    a.read_weibo()
elif '3' in file_name:
    a.read_pinglun()
a.mood()
a.ciyun()
