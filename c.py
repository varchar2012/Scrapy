import random
from random import randint
import pymysql
# db = pymysql.connect("localhost","root","root","ticai")
# cursor = db.cursor()
#1~35出现的概率列表

index = 0

arr = range(1,13)
rate = [22,33,44,223,324,12,323,33,55,555,77,321]

randnum =sorted(random.sample(range(1,sum(rate)),5))
x = randnum

def random_index(rate,r,i):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    for index, scope in enumerate(rate):
        start = start + scope
   
        if r[i] <= start:
           
            break
    return index
    
       
    
 
print(arr[random_index(rate,x,0)],arr[random_index(rate,x,1)],arr[random_index(rate,x,2)],arr[random_index(rate,x,3)],arr[random_index(rate,x,4)])



