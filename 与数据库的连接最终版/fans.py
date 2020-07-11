import pymysql
#设置列表和字典
fans_list=['0-200','200-500','500-1000','1000-2000','2000-3000','3000-5000','5000-8000','8000-10000','10000-']
fans_dict={'0-200':0,'200-500':0,'500-1000':0,'1000-2000':0,'2000-3000':0,'3000-5000':0,'5000-8000':0,'8000-10000':0,'10000-':0}
#与数据库连接
db=pymysql.connect("localhost","root","","test")
#设置游标
cursor=db.cursor()
#mysql语句查询每个用户的粉丝数量
sql="select fans from weibo"
#执行mysql
cursor.execute(sql)
#获取查询的所有结果
result=cursor.fetchall()
#关闭游标
db.close()
for i in range(0,1305):
    fans=int(result[i][0])#将粉丝数据类型转换为int，便于比较大小
    #对粉丝数量确定区间
    if fans<200:
        fans_dict['0-200']=fans_dict['0-200']+1
    elif 200<=fans<500:
        fans_dict['200-500']=fans_dict['200-500']+1
    elif 500<=fans<1000:
        fans_dict['500-1000']=fans_dict['500-1000']+1
    elif 1000<=fans<2000:
        fans_dict['1000-2000']=fans_dict['1000-2000']+1
    elif 2000<=fans<3000:
        fans_dict['2000-3000']=fans_dict['2000-3000']+1
    elif 3000<=fans<5000:
        fans_dict['3000-5000']=fans_dict['3000-5000']+1
    elif 5000<=fans<8000:
        fans_dict['5000-8000']=fans_dict['5000-8000']+1
    elif 8000<=fans<10000:
        fans_dict['8000-10000']=fans_dict['8000-10000']+1
    else:
        fans_dict['10000-']=fans_dict['10000-']+1
for i in fans_list:
    print(i)
    print(fans_dict[i])
