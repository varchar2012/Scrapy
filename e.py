import random
from random import randint
import pymysql
db = pymysql.connect("localhost","root","root","ticai")
cursor = db.cursor()

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
    g1 = ['f_one','f_two','f_three','f_four','f_five']
    g2 = ['r_one','r_two']
    for a in g1:
        for b in arr:
            sql = """SELECT COUNT(%s) FROM daletou WHERE %s = %s""" % (a,a,b)
            
            cursor.execute(sql)
            z1 = list(cursor.fetchone())
            rate = z1+rate
            db.close()
    rate1 = sum(rate[0:31])
    print(rate1)
    a = 0
    r_number = []
    while a<500 :
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE f_one % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index(rate)
    #按照奇数偶数概率进行计算
    col = []
    if mi1 == 0:
        for i in r_number:
            if (i % 2) == 0:
                col.append(i)
                # print(i)
            else:
                continue
    else:
        for x in r_number:
            if (x % 2) == 1:
                col.append(x)
                # print(x)           
                # print(r_number[mi1])
            else:
                continue
    # print(col)
    # print(arr[random_index(rate)])
    # 按照区间概率计算
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 1 AND 5"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 6 AND 10"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE f_one BETWEEN 31 AND 35"""
    cursor.execute(qujian1_5)
    qujian1_5 = list(cursor.fetchone())
    cursor.execute(qujian6_10)
    qujian6_10  = list(cursor.fetchone())
    cursor.execute(qujian11_15)
    qujian11_15 = list(cursor.fetchone())
    cursor.execute(qujian16_20)
    qujian16_20 = list(cursor.fetchone())
    cursor.execute(qujian21_25)
    qujian21_25 = list(cursor.fetchone())
    cursor.execute(qujian26_30)
    qujian26_30 = list(cursor.fetchone())
    cursor.execute(qujian31_35)
    qujian31_35 = list(cursor.fetchone())
    rate = qujian1_5+qujian6_10+qujian11_15+qujian16_20+qujian21_25+qujian26_30+qujian31_35
    mi2 = random_index(rate)
    col1 = []
    if mi2 == 0:
        for x in col:
            if x < 6:
                col1.append(x)
            else:
                continue
    elif mi2 == 1:
        for x in col:
            if x>5 and x < 11:
                col1.append(x)
            else:
                continue
    elif mi2 == 2:
        for x in col:
            if x>10 and x < 16:
                col1.append(x)
            else:
                continue
    elif mi2 == 3:
        for x in col:
            if x>15 and x < 21:
                col1.append(x)
            else:
                continue
    elif mi2 == 4:
        for x in col:
            if x>20 and x < 26:
                col1.append(x)
            else:
                continue
    elif mi2 == 5:
        for x in col:
            if x>25 and x < 31:
                col1.append(x)
            else:
                continue
    elif mi2 == 6:
        for x in col:
            if x>30 and x < 36:
                col1.append(x)
            else:
                continue                                            
    print(col1,end = '!!!')
    return col1







arr = [x for x in range(1,36)]
arr2 = [x for x in range(1,13)]

arr1 = [1,2,3,4,5,6,7,8]
rate = []
g1 = ['f_one','f_two','f_three','f_four','f_five']
g2 = ['r_one','r_two']
for a in g1:
    for b in arr:
        sql = """SELECT COUNT(%s) FROM daletou WHERE %s = %s""" % (a,a,b)
        
        cursor.execute(sql)
        z1 = list(cursor.fetchone())
        rate = z1+rate
        # print(z1)
# print(rate[0:3])        


# for a in g2:
#     for b in arr2:
#         sql2 =   """SELECT COUNT(%s) FROM daletou WHERE %s = %s""" % (a,a,b)      
#         print(sql2)