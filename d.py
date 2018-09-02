import random
from random import randint
import numpy as np 
import pymysql
db = pymysql.connect("localhost","root","root","ticai")
cursor = db.cursor()
rate = list(range(1,36))
#计算号码出现次数

z = []
for b in rate:
    sql = """SELECT COUNT(*) FROM ticai.daletou WHERE f_one = %s OR f_two = %s OR f_three = %s OR f_four = %s OR f_five = %s""" %(b,b,b,b,b)
    cursor.execute(sql)
    z1 = list(cursor.fetchone())
    z = z1+z
    
#计算号码总和、概率
db.close() 
c = []

for x in list(reversed(z)):
    y = x/sum(z)
    c.append(y)

p =0
while p<100:
    w = np.random.choice(rate,size=(1,5),replace=False,p=c)[0]
    ww = sorted(w)
    print(list(ww))
    p += 1