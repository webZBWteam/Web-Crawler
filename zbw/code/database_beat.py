#coding=utf-8
import sys
import pymysql
if __name__ == "__main__":
  conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='asdf1234', db='experiment1', charset='utf8')
  conn.begin()
  cursor = conn.cursor()
  idd=input('please input the transaction id:')
  item = input('please input the item id:')
  customer=input('please input the customer id:')
  date=input('please input the date:')
  number=input('please input the number you bought the item:')
  price=input('please input the price:')
  s='("'+idd+'","'+item+'","'+customer+'","'+date+'",'+number+','+price+')'
  print(s)
  try:
    cursor.execute("INSERT INTO S_DD VALUES"+s)
  except:
    conn.rollback()
    print('error! integrity constraint! execute rollback')
    conn.close()
    exit(0)
  try:
    cursor.execute("SELECT `SPFC` FROM S_SP WHERE `SPBH`='"+item+"'")
    result=cursor.fetchall()
    result=list(result[0])
    if result[0]<eval(number):
      conn.rollback()
      exit(0)
  except:
    conn.rollback()
    print('error! exceed the amount of storage! execute rollback')
  try:
    s="UPDATE S_SP SET `SPFC`=`SPFC`-"+number+" WHERE `SPBH` LIKE '"+item+"'"
    print(s)
    cursor.execute(s)
  except:
    conn.rollback()
    print('error!')
    exit(0)
  conn.commit()
