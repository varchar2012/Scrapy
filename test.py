import random
from random import randint
import pymysql
db = pymysql.connect("localhost","root","root","ticai")
cursor = db.cursor()
col = []
col2 = []
aa = [] 
def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index

def main():
    arr = [x for x in range(1,36)]
    rate = []
    rate2 = []
    # 前区概率
    g1 = ['f_one','f_two','f_three','f_four','f_five']
    for a in g1:
        for b in arr:
            sql = """SELECT COUNT(%s) FROM daletou WHERE %s = %s""" % (a,a,b)
            cursor.execute(sql)
            z1 = list(cursor.fetchone())
            rate = z1+rate
            
    rate = list(reversed(rate))
    #后区概率
    arr2 = [x for x in range(1,13)]
    g2 = ['r_one','r_two']
    for a in g2:
        for b in arr2:
            sql = """SELECT COUNT(%s) FROM daletou WHERE %s = %s""" % (a,a,b)
            
            cursor.execute(sql)
            z2 = list(cursor.fetchone())
            rate2 = z2+rate2
    rate2 = list(reversed(rate2))
 
    rate = rate +rate2
   
  
  
    a = 0
    r_number1 = []
    r_number2 = []
    r_number3 = []
    r_number4 = []
    r_number5 = []
    r_number6 = []
    r_number7 = []
    r_number = zip(r_number1,r_number2,r_number3,r_number4,r_number5,r_number6,r_number7)
    # 生成号码
    while a<500 :
        
        # print(arr[random_index(rate)])
        r_number1.append(arr[random_index(rate[0:35])])
        r_number2.append(arr[random_index(rate[35:70])])
        r_number3.append(arr[random_index(rate[70:105])])
        r_number4.append(arr[random_index(rate[105:140])])
        r_number5.append(arr[random_index(rate[140:175])])
        r_number6.append(arr[random_index(rate[175:187])])
        r_number7.append(arr[random_index(rate[187:199])])
        
        a= a+1
    # print(r_number1)
    '''奇数偶数概率'''
    jishu1 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu1)
    jishu1 = list(cursor.fetchone())
   
    oushu1 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu1)
    oushu1 = list(cursor.fetchone())
   
    jishu2 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu2)
    jishu2 = list(cursor.fetchone())
    
    oushu2 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu2)
    oushu2 = list(cursor.fetchone())
    
    jishu3 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu3)
    jishu3 = list(cursor.fetchone())
  
    oushu3 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu3)
    oushu3 = list(cursor.fetchone())
    
    jishu4 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu4)
    jishu4 = list(cursor.fetchone())
  
    oushu4 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu4)
    oushu4 = list(cursor.fetchone())
   
    jishu5 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu5)
    jishu5 = list(cursor.fetchone())

    oushu5 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu5)
    oushu5 = list(cursor.fetchone())
    
    jishu6 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu6)
    jishu6 = list(cursor.fetchone())
    
    oushu6 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu6)
    oushu6 = list(cursor.fetchone())

    jishu7 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1""" 
    cursor.execute(jishu7)
    jishu7 = list(cursor.fetchone())
  
    oushu7 = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
    cursor.execute(oushu7)
    oushu7 = list(cursor.fetchone())
    db.close() 


    rate1 = jishu1+oushu1+jishu2+oushu2+jishu3+oushu3+jishu4+oushu4+jishu5+oushu5+jishu6+oushu6+jishu7+oushu7

    mi1 = random_index(rate1[0:2])
    mi2 = random_index(rate1[2:4])
    mi3 = random_index(rate1[4:6])
    mi4 = random_index(rate1[6:8])
    mi5 = random_index(rate1[8:10])
    mi6 = random_index(rate1[10:12])
    mi7 = random_index(rate1[12:14])
    

    misum = [mi1,mi2,mi3,mi4,mi5,mi6,mi7]
    # print(misum[0])
    
   
    
    # su = dict(zip(r_number,misum))
    # print(su)
    # f = [x for x in range(7)]
    
    for r,m in  zip(r_number,misum):
        
        
        # for j in r:
        #     print(j)
        
        st1 = [x for x in r if x % 2 == 0]
        # print(st1)
        # col2.append(st1)
    
        st2 = [x for x in r if x % 2 == 1]   
       
        xx = st1 if m == 0 else st2
        aa.append(xx)
       




        
               
    # for x in st1:
    #     # print(x)
    #     if x[1] == 0:
    #         for i in x[0]:
    #             if i % 2 == 0:
    #                 col.append(i)
    #             elif i % 2 == 1:
    #                 continue 
    #     elif x[1] == 1:
    #         for i in x[0]:
    #             if i % 2 == 1:
    #                 col.append(i)
    #             elif i % 2 == 0:
    #                 continue                        

main() 
print(aa) 

