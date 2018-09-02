# a = [1,1,2,3,4,545,64,3,2,1]
# print(a)

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

def random_index2(rate):
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
def random_index3(rate):
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

def random_index4(rate):
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
def random_index5(rate):
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
def random_index6(rate):
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
def random_index7(rate):
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
    arr = [x for x in range(1,31)]

    rate = []
    try:
        g1 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 1"""
        g2 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 2"""
        g3 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 3"""
        g4 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 4"""
        g5 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 5"""
        g6 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 6"""
        g7 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 7"""
        g8 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 8"""
        g9 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 9"""
        g10 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 10"""
        g11 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 11"""
        g12 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 12"""
        g13 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 13"""
        g14 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 14"""
        g15 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 15"""
        g16 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 16"""
        g17 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 17"""
        g18 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 18"""
        g19 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 19"""
        g20 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 20"""
        g21 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 21"""
        g22 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 22"""
        g23 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 23"""
        g24 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 24"""
        g25 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 25"""
        g26 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 26"""
        g27 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 27"""
        g28 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 28"""
        g29 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 29"""
        g30 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 30"""
        g31 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 31"""
        # g32 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 32"""
        # g33 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 33"""
        # g34 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 34"""
        # g35 = """SELECT COUNT(f_one) FROM daletou WHERE f_one = 35"""

        cursor.execute(g1)
        g1 = list(cursor.fetchone())
        cursor.execute(g2)
        g2 = list(cursor.fetchone())
        cursor.execute(g3)
        g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        cursor.execute(g13)
        g13 = list(cursor.fetchone())
        cursor.execute(g14)
        g14 = list(cursor.fetchone())
        cursor.execute(g15)
        g15 = list(cursor.fetchone())
        cursor.execute(g16)
        g16 = list(cursor.fetchone())
        cursor.execute(g17)
        g17 = list(cursor.fetchone())
        cursor.execute(g18)
        g18 = list(cursor.fetchone())
        cursor.execute(g19)
        g19 = list(cursor.fetchone())
        cursor.execute(g20)
        g20 = list(cursor.fetchone())
        cursor.execute(g21)
        g21 = list(cursor.fetchone())
        cursor.execute(g22)
        g22 = list(cursor.fetchone())
        cursor.execute(g23)
        g23 = list(cursor.fetchone())
        cursor.execute(g24)
        g24 = list(cursor.fetchone())
        cursor.execute(g25)
        g25 = list(cursor.fetchone())
        cursor.execute(g26)
        g26 = list(cursor.fetchone())
        cursor.execute(g27)
        g27 = list(cursor.fetchone())
        cursor.execute(g28)
        g28 = list(cursor.fetchone())
        cursor.execute(g29)
        g29 = list(cursor.fetchone())
        cursor.execute(g30)
        g30 = list(cursor.fetchone())
        cursor.execute(g31)
        g31 = list(cursor.fetchone())
        # cursor.execute(g32)
        # g32 = list(cursor.fetchone())
        # cursor.execute(g33)
        # g33 = list(cursor.fetchone())
        # cursor.execute(g34)
        # g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15+g16+g17+g18+g19+g20+g21+g22+g23+g24+g25+g26+g27+g28+g29+g30+g31
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


def main2():
    arr = [x for x in range(2,32)]

    rate = []
    try:
        # g1 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 1"""
        g2 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 2"""
        g3 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two  = 3"""
        g4 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 4"""
        g5 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 5"""
        g6 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 6"""
        g7 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 7"""
        g8 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 8"""
        g9 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 9"""
        g10 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 10"""
        g11 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 11"""
        g12 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 12"""
        g13 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 13"""
        g14 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 14"""
        g15 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 15"""
        g16 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 16"""
        g17 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 17"""
        g18 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 18"""
        g19 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 19"""
        g20 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 20"""
        g21 = """SELECT COUNT(f_two ) FROM daletou WHERE f_two = 21"""
        g22 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 22"""
        g23 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 23"""
        g24 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 24"""
        g25 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 25"""
        g26 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 26"""
        g27 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 27"""
        g28 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 28"""
        g29 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 29"""
        g30 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 30"""
        g31 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 31"""
        g32 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 32"""
        # g33 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 33"""
        # g34 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 34"""
        # g35 = """SELECT COUNT(f_two) FROM daletou WHERE f_two = 35"""

        # cursor.execute(g1)
        # g1 = list(cursor.fetchone())
        cursor.execute(g2)
        g2 = list(cursor.fetchone())
        cursor.execute(g3)
        g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        cursor.execute(g13)
        g13 = list(cursor.fetchone())
        cursor.execute(g14)
        g14 = list(cursor.fetchone())
        cursor.execute(g15)
        g15 = list(cursor.fetchone())
        cursor.execute(g16)
        g16 = list(cursor.fetchone())
        cursor.execute(g17)
        g17 = list(cursor.fetchone())
        cursor.execute(g18)
        g18 = list(cursor.fetchone())
        cursor.execute(g19)
        g19 = list(cursor.fetchone())
        cursor.execute(g20)
        g20 = list(cursor.fetchone())
        cursor.execute(g21)
        g21 = list(cursor.fetchone())
        cursor.execute(g22)
        g22 = list(cursor.fetchone())
        cursor.execute(g23)
        g23 = list(cursor.fetchone())
        cursor.execute(g24)
        g24 = list(cursor.fetchone())
        cursor.execute(g25)
        g25 = list(cursor.fetchone())
        cursor.execute(g26)
        g26 = list(cursor.fetchone())
        cursor.execute(g27)
        g27 = list(cursor.fetchone())
        cursor.execute(g28)
        g28 = list(cursor.fetchone())
        cursor.execute(g29)
        g29 = list(cursor.fetchone())
        cursor.execute(g30)
        g30 = list(cursor.fetchone())
        cursor.execute(g31)
        g31 = list(cursor.fetchone())
        cursor.execute(g32)
        g32 = list(cursor.fetchone())
        # cursor.execute(g33)
        # g33 = list(cursor.fetchone())
        # cursor.execute(g34)
        # g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g2+g3+g4+g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15+g16+g17+g18+g19+g20+g21+g22+g23+g24+g25+g26+g27+g28+g29+g30+g31+g32
    a = 0
    r_number2 = []
    while a<50000 :
        
        # print(arr[random_index(rate)])
        r_number2.append(arr[random_index2(rate)])
        a= a+1

    
    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE f_two % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE f_two % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index2(rate)
    #按照奇数偶数概率进行计算
    col = []
    if mi1 == 0:
        for i in r_number2:
            if (i % 2) == 0:
                col.append(i)
                # print(i)
            else:
                continue
    else:
        for x in r_number2:
            if (x % 2) == 1:
                col.append(x)
                # print(x)           
                # print(r_number[mi1])
            else:
                continue
    # print(col)
    # print(arr[random_index(rate)])
    # 按照区间概率计算
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 1 AND 5"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 6 AND 10"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE f_two BETWEEN 31 AND 35"""
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
    mi2 = random_index2(rate)
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
    print(col1,end = '222')
    return col1

def main3():
    arr = [x for x in range(3,33)]

    rate = []
    try:
        # g1 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 1"""
        # g2 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 2"""
        g3 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 3"""
        g4 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 4"""
        g5 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 5"""
        g6 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 6"""
        g7 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 7"""
        g8 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 8"""
        g9 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 9"""
        g10 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 10"""
        g11 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 11"""
        g12 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 12"""
        g13 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 13"""
        g14 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 14"""
        g15 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 15"""
        g16 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 16"""
        g17 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 17"""
        g18 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 18"""
        g19 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 19"""
        g20 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 20"""
        g21 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 21"""
        g22 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 22"""
        g23 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 23"""
        g24 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 24"""
        g25 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 25"""
        g26 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 26"""
        g27 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 27"""
        g28 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 28"""
        g29 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 29"""
        g30 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 30"""
        g31 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 31"""
        g32 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 32"""
        g33 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 33"""
        # g34 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 34"""
        # g35 = """SELECT COUNT(f_three) FROM daletou WHERE f_three = 35"""

        # cursor.execute(g1)
        # g1 = list(cursor.fetchone())
        # cursor.execute(g2)
        # g2 = list(cursor.fetchone())
        cursor.execute(g3)
        g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        cursor.execute(g13)
        g13 = list(cursor.fetchone())
        cursor.execute(g14)
        g14 = list(cursor.fetchone())
        cursor.execute(g15)
        g15 = list(cursor.fetchone())
        cursor.execute(g16)
        g16 = list(cursor.fetchone())
        cursor.execute(g17)
        g17 = list(cursor.fetchone())
        cursor.execute(g18)
        g18 = list(cursor.fetchone())
        cursor.execute(g19)
        g19 = list(cursor.fetchone())
        cursor.execute(g20)
        g20 = list(cursor.fetchone())
        cursor.execute(g21)
        g21 = list(cursor.fetchone())
        cursor.execute(g22)
        g22 = list(cursor.fetchone())
        cursor.execute(g23)
        g23 = list(cursor.fetchone())
        cursor.execute(g24)
        g24 = list(cursor.fetchone())
        cursor.execute(g25)
        g25 = list(cursor.fetchone())
        cursor.execute(g26)
        g26 = list(cursor.fetchone())
        cursor.execute(g27)
        g27 = list(cursor.fetchone())
        cursor.execute(g28)
        g28 = list(cursor.fetchone())
        cursor.execute(g29)
        g29 = list(cursor.fetchone())
        cursor.execute(g30)
        g30 = list(cursor.fetchone())
        cursor.execute(g31)
        g31 = list(cursor.fetchone())
        cursor.execute(g32)
        g32 = list(cursor.fetchone())
        cursor.execute(g33)
        g33 = list(cursor.fetchone())
        # cursor.execute(g34)
        # g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g3+g4+g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15+g16+g17+g18+g19+g20+g21+g22+g23+g24+g25+g26+g27+g28+g29+g30+g31+g32+g33
    a = 0
    r_number = []
    while a<50000 :
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index3(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE f_three % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE f_three % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index3(rate)
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
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 1 AND 5"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 6 AND 10"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE f_three BETWEEN 31 AND 35"""
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
    mi2 = random_index3(rate)
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
    print(col1,end = '333')
    return col1
def main4():
    arr = [x for x in range(4,34)]

    rate = []
    try:
        # g1 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 1"""
        # g2 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 2"""
        # g3 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 3"""
        g4 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 4"""
        g5 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 5"""
        g6 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 6"""
        g7 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 7"""
        g8 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 8"""
        g9 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 9"""
        g10 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 10"""
        g11 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 11"""
        g12 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 12"""
        g13 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 13"""
        g14 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 14"""
        g15 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 15"""
        g16 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 16"""
        g17 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 17"""
        g18 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 18"""
        g19 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 19"""
        g20 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 20"""
        g21 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 21"""
        g22 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 22"""
        g23 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 23"""
        g24 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 24"""
        g25 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 25"""
        g26 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 26"""
        g27 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 27"""
        g28 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 28"""
        g29 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 29"""
        g30 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 30"""
        g31 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 31"""
        g32 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 32"""
        g33 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 33"""
        g34 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 34"""
        # g35 = """SELECT COUNT(f_four) FROM daletou WHERE f_four = 35"""

        # cursor.execute(g1)
        # g1 = list(cursor.fetchone())
        # cursor.execute(g2)
        # g2 = list(cursor.fetchone())
        # cursor.execute(g3)
        # g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        cursor.execute(g13)
        g13 = list(cursor.fetchone())
        cursor.execute(g14)
        g14 = list(cursor.fetchone())
        cursor.execute(g15)
        g15 = list(cursor.fetchone())
        cursor.execute(g16)
        g16 = list(cursor.fetchone())
        cursor.execute(g17)
        g17 = list(cursor.fetchone())
        cursor.execute(g18)
        g18 = list(cursor.fetchone())
        cursor.execute(g19)
        g19 = list(cursor.fetchone())
        cursor.execute(g20)
        g20 = list(cursor.fetchone())
        cursor.execute(g21)
        g21 = list(cursor.fetchone())
        cursor.execute(g22)
        g22 = list(cursor.fetchone())
        cursor.execute(g23)
        g23 = list(cursor.fetchone())
        cursor.execute(g24)
        g24 = list(cursor.fetchone())
        cursor.execute(g25)
        g25 = list(cursor.fetchone())
        cursor.execute(g26)
        g26 = list(cursor.fetchone())
        cursor.execute(g27)
        g27 = list(cursor.fetchone())
        cursor.execute(g28)
        g28 = list(cursor.fetchone())
        cursor.execute(g29)
        g29 = list(cursor.fetchone())
        cursor.execute(g30)
        g30 = list(cursor.fetchone())
        cursor.execute(g31)
        g31 = list(cursor.fetchone())
        cursor.execute(g32)
        g32 = list(cursor.fetchone())
        cursor.execute(g33)
        g33 = list(cursor.fetchone())
        cursor.execute(g34)
        g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g4+g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15+g16+g17+g18+g19+g20+g21+g22+g23+g24+g25+g26+g27+g28+g29+g30+g31+g32+g33+g34
    a = 0
    r_number = []
    while a<500:
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index4(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE f_four % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE f_four % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index4(rate)
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
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 1 AND 5"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 6 AND 10"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE f_four BETWEEN 31 AND 35"""
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
    mi2 = random_index4(rate)
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
    print(col1,end = '444')
    return col1
def main5():
    arr = [x for x in range(5,35)]

    rate = []
    try:
        # g1 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 1"""
        # g2 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 2"""
        # g3 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 3"""
        # g4 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 4"""
        g5 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 5"""
        g6 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 6"""
        g7 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 7"""
        g8 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 8"""
        g9 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 9"""
        g10 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 10"""
        g11 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 11"""
        g12 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 12"""
        g13 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 13"""
        g14 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 14"""
        g15 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 15"""
        g16 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 16"""
        g17 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 17"""
        g18 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 18"""
        g19 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 19"""
        g20 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 20"""
        g21 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 21"""
        g22 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 22"""
        g23 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 23"""
        g24 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 24"""
        g25 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 25"""
        g26 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 26"""
        g27 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 27"""
        g28 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 28"""
        g29 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 29"""
        g30 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 30"""
        g31 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 31"""
        g32 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 32"""
        g33 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 33"""
        g34 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 34"""
        g35 = """SELECT COUNT(f_five) FROM daletou WHERE f_five = 35"""

        # cursor.execute(g1)
        # g1 = list(cursor.fetchone())
        # cursor.execute(g2)
        # g2 = list(cursor.fetchone())
        # cursor.execute(g3)
        # g3 = list(cursor.fetchone())
        # cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        cursor.execute(g13)
        g13 = list(cursor.fetchone())
        cursor.execute(g14)
        g14 = list(cursor.fetchone())
        cursor.execute(g15)
        g15 = list(cursor.fetchone())
        cursor.execute(g16)
        g16 = list(cursor.fetchone())
        cursor.execute(g17)
        g17 = list(cursor.fetchone())
        cursor.execute(g18)
        g18 = list(cursor.fetchone())
        cursor.execute(g19)
        g19 = list(cursor.fetchone())
        cursor.execute(g20)
        g20 = list(cursor.fetchone())
        cursor.execute(g21)
        g21 = list(cursor.fetchone())
        cursor.execute(g22)
        g22 = list(cursor.fetchone())
        cursor.execute(g23)
        g23 = list(cursor.fetchone())
        cursor.execute(g24)
        g24 = list(cursor.fetchone())
        cursor.execute(g25)
        g25 = list(cursor.fetchone())
        cursor.execute(g26)
        g26 = list(cursor.fetchone())
        cursor.execute(g27)
        g27 = list(cursor.fetchone())
        cursor.execute(g28)
        g28 = list(cursor.fetchone())
        cursor.execute(g29)
        g29 = list(cursor.fetchone())
        cursor.execute(g30)
        g30 = list(cursor.fetchone())
        cursor.execute(g31)
        g31 = list(cursor.fetchone())
        cursor.execute(g32)
        g32 = list(cursor.fetchone())
        cursor.execute(g33)
        g33 = list(cursor.fetchone())
        cursor.execute(g34)
        g34 = list(cursor.fetchone())
        cursor.execute(g35)
        g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g5+g6+g7+g8+g9+g10+g11+g12+g13+g14+g15+g16+g17+g18+g19+g20+g21+g22+g23+g24+g25+g26+g27+g28+g29+g30+g31+g32+g33+g34+g35
    a = 0
    r_number = []
    while a<500 :
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index5(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE f_five % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE f_five % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index5(rate)
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
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 1 AND 5"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 6 AND 10"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE f_five BETWEEN 31 AND 35"""
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
    mi2 = random_index5(rate)
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
    print(col1,end = '555')
    return col1
def mainb1():
    arr = [x for x in range(1,11)]

    rate = []
    try:
        g1 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 1"""
        g2 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 2"""
        g3 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 3"""
        g4 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 4"""
        g5 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 5"""
        g6 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 6"""
        g7 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 7"""
        g8 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 8"""
        g9 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 9"""
        g10 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 10"""
        g11 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 11"""
        # g12 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 12"""
        # g13 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 13"""
        # g14 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 14"""
        # g15 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 15"""
        # g16 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 16"""
        # g17 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 17"""
        # g18 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 18"""
        # g19 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 19"""
        # g20 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 20"""
        # g21 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 21"""
        # g22 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 22"""
        # g23 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 23"""
        # g24 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 24"""
        # g25 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 25"""
        # g26 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 26"""
        # g27 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 27"""
        # g28 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 28"""
        # g29 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 29"""
        # g30 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 30"""
        # g31 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 31"""
        # g32 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 32"""
        # g33 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 33"""
        # g34 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 34"""
        # g35 = """SELECT COUNT(r_one) FROM daletou WHERE r_one = 35"""

        cursor.execute(g1)
        g1 = list(cursor.fetchone())
        cursor.execute(g2)
        g2 = list(cursor.fetchone())
        cursor.execute(g3)
        g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        # cursor.execute(g12)
        # g12 = list(cursor.fetchone())
        # cursor.execute(g13)
        # g13 = list(cursor.fetchone())
        # cursor.execute(g14)
        # g14 = list(cursor.fetchone())
        # cursor.execute(g15)
        # g15 = list(cursor.fetchone())
        # cursor.execute(g16)
        # g16 = list(cursor.fetchone())
        # cursor.execute(g17)
        # g17 = list(cursor.fetchone())
        # cursor.execute(g18)
        # g18 = list(cursor.fetchone())
        # cursor.execute(g19)
        # g19 = list(cursor.fetchone())
        # cursor.execute(g20)
        # g20 = list(cursor.fetchone())
        # cursor.execute(g21)
        # g21 = list(cursor.fetchone())
        # cursor.execute(g22)
        # g22 = list(cursor.fetchone())
        # cursor.execute(g23)
        # g23 = list(cursor.fetchone())
        # cursor.execute(g24)
        # g24 = list(cursor.fetchone())
        # cursor.execute(g25)
        # g25 = list(cursor.fetchone())
        # cursor.execute(g26)
        # g26 = list(cursor.fetchone())
        # cursor.execute(g27)
        # g27 = list(cursor.fetchone())
        # cursor.execute(g28)
        # g28 = list(cursor.fetchone())
        # cursor.execute(g29)
        # g29 = list(cursor.fetchone())
        # cursor.execute(g30)
        # g30 = list(cursor.fetchone())
        # cursor.execute(g31)
        # g31 = list(cursor.fetchone())
        # # cursor.execute(g32)
        # g32 = list(cursor.fetchone())
        # cursor.execute(g33)
        # g33 = list(cursor.fetchone())
        # cursor.execute(g34)
        # g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g1+g2+g3+g4+g5+g6+g7+g8+g9+g10+g11
    a = 0
    r_number = []
    while a<500 :
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index6(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE r_one % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE r_one % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index6(rate)
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
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 1 AND 6"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 7 AND 12"""
    # qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 11 AND 15"""
    # qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 16 AND 20"""
    # qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 21 AND 25"""
    # qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 26 AND 30"""
    # qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE r_one BETWEEN 31 AND 35"""
    cursor.execute(qujian1_5)
    qujian1_5 = list(cursor.fetchone())
    cursor.execute(qujian6_10)
    qujian6_10  = list(cursor.fetchone())
    # cursor.execute(qujian11_15)
    # qujian11_15 = list(cursor.fetchone())
    # cursor.execute(qujian16_20)
    # qujian16_20 = list(cursor.fetchone())
    # cursor.execute(qujian21_25)
    # qujian21_25 = list(cursor.fetchone())
    # cursor.execute(qujian26_30)
    # qujian26_30 = list(cursor.fetchone())
    # cursor.execute(qujian31_35)
    # qujian31_35 = list(cursor.fetchone())
    rate = qujian1_5+qujian6_10
    mi2 = random_index6(rate)
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
    # elif mi2 == 2:
    #     for x in col:
    #         if x>10 and x < 16:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 3:
    #     for x in col:
    #         if x>15 and x < 21:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 4:
    #     for x in col:
    #         if x>20 and x < 26:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 5:
    #     for x in col:
    #         if x>25 and x < 31:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 6:
        for x in col:
            if x>30 and x < 36:
                col1.append(x)
            else:
                continue                                            
    print(col1,end = '~1')
    return col1
def mainb2():
    arr = [x for x in range(2,12)]

    rate = []
    try:
        # g1 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 1"""
        g2 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 2"""
        g3 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 3"""
        g4 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 4"""
        g5 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 5"""
        g6 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 6"""
        g7 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 7"""
        g8 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 8"""
        g9 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 9"""
        g10 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 10"""
        g11 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 11"""
        g12 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 12"""
        # g13 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 13"""
        # g14 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 14"""
        # g15 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 15"""
        # g16 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 16"""
        # g17 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 17"""
        # g18 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 18"""
        # g19 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 19"""
        # g20 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 20"""
        # g21 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 21"""
        # g22 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 22"""
        # g23 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 23"""
        # g24 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 24"""
        # g25 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 25"""
        # g26 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 26"""
        # g27 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 27"""
        # g28 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 28"""
        # g29 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 29"""
        # g30 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 30"""
        # g31 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 31"""
        # g32 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 32"""
        # g33 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 33"""
        # g34 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 34"""
        # g35 = """SELECT COUNT(r_two) FROM daletou WHERE r_two = 35"""

        # cursor.execute(g1)
        # g1 = list(cursor.fetchone())
        cursor.execute(g2)
        g2 = list(cursor.fetchone())
        cursor.execute(g3)
        g3 = list(cursor.fetchone())
        cursor.execute(g4)
        g4 = list(cursor.fetchone())
        cursor.execute(g5)
        g5 = list(cursor.fetchone())
        cursor.execute(g6)
        g6 = list(cursor.fetchone())
        cursor.execute(g7)
        g7 = list(cursor.fetchone())
        cursor.execute(g8)
        g8 = list(cursor.fetchone())
        cursor.execute(g9)
        g9 = list(cursor.fetchone())
        cursor.execute(g10)
        g10 = list(cursor.fetchone())
        cursor.execute(g11)
        g11 = list(cursor.fetchone())
        cursor.execute(g12)
        g12 = list(cursor.fetchone())
        # cursor.execute(g13)
        # g13 = list(cursor.fetchone())
        # cursor.execute(g14)
        # g14 = list(cursor.fetchone())
        # cursor.execute(g15)
        # g15 = list(cursor.fetchone())
        # cursor.execute(g16)
        # g16 = list(cursor.fetchone())
        # cursor.execute(g17)
        # g17 = list(cursor.fetchone())
        # cursor.execute(g18)
        # g18 = list(cursor.fetchone())
        # cursor.execute(g19)
        # g19 = list(cursor.fetchone())
        # cursor.execute(g20)
        # g20 = list(cursor.fetchone())
        # cursor.execute(g21)
        # g21 = list(cursor.fetchone())
        # cursor.execute(g22)
        # g22 = list(cursor.fetchone())
        # cursor.execute(g23)
        # g23 = list(cursor.fetchone())
        # cursor.execute(g24)
        # g24 = list(cursor.fetchone())
        # cursor.execute(g25)
        # g25 = list(cursor.fetchone())
        # cursor.execute(g26)
        # g26 = list(cursor.fetchone())
        # cursor.execute(g27)
        # g27 = list(cursor.fetchone())
        # cursor.execute(g28)
        # g28 = list(cursor.fetchone())
        # cursor.execute(g29)
        # g29 = list(cursor.fetchone())
        # cursor.execute(g30)
        # g30 = list(cursor.fetchone())
        # cursor.execute(g31)
        # g31 = list(cursor.fetchone())
        # cursor.execute(g32)
        # g32 = list(cursor.fetchone())
        # cursor.execute(g33)
        # g33 = list(cursor.fetchone())
        # cursor.execute(g34)
        # g34 = list(cursor.fetchone())
        # cursor.execute(g35)
        # g35 = list(cursor.fetchone())
    except:
        db.rollback()

        db.close()     
        
    rate = g2+g3+g4+g5+g6+g7+g8+g9+g10+g11+g12
    a = 0
    r_number = []
    while a<500 :
        
        # print(arr[random_index(rate)])
        r_number.append(arr[random_index7(rate)])
        a= a+1

    # print(r_number)            

    try:
        jishu = """SELECT COUNT(*) FROM daletou WHERE r_two % 2 = 1"""
        cursor.execute(jishu)
        jishu = list(cursor.fetchone())
        # print(jishu)
    except :
        db.rollback()

        db.close()   
    try:
        oushu = """SELECT COUNT(*) FROM daletou WHERE r_two % 2 = 0"""
        cursor.execute(oushu)
        oushu = list(cursor.fetchone())
        # print(oushu)
    except :
        db.rollback()

        db.close()  
    
    rate = jishu+oushu
    mi1 = random_index7(rate)
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
    qujian1_5 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 2 AND 6"""
    qujian6_10 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 7 AND 12"""
    qujian11_15 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 11 AND 15"""
    qujian16_20 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 16 AND 20"""
    qujian21_25 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 21 AND 25"""
    qujian26_30 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 26 AND 30"""
    qujian31_35 = """SELECT COUNT(*) FROM daletou WHERE r_two BETWEEN 31 AND 35"""
    cursor.execute(qujian1_5)
    qujian1_5 = list(cursor.fetchone())
    cursor.execute(qujian6_10)
    qujian6_10  = list(cursor.fetchone())
    # cursor.execute(qujian11_15)
    # qujian11_15 = list(cursor.fetchone())
    # cursor.execute(qujian16_20)
    # qujian16_20 = list(cursor.fetchone())
    # cursor.execute(qujian21_25)
    # qujian21_25 = list(cursor.fetchone())
    # cursor.execute(qujian26_30)
    # qujian26_30 = list(cursor.fetchone())
    # cursor.execute(qujian31_35)
    # qujian31_35 = list(cursor.fetchone())
    rate = qujian1_5+qujian6_10
    mi2 = random_index7(rate)
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
    # elif mi2 == 2:
    #     for x in col:
    #         if x>10 and x < 16:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 3:
    #     for x in col:
    #         if x>15 and x < 21:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 4:
    #     for x in col:
    #         if x>20 and x < 26:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 5:
    #     for x in col:
    #         if x>25 and x < 31:
    #             col1.append(x)
    #         else:
    #             continue
    # elif mi2 == 6:
        # for x in col:
        #     if x>30 and x < 36:
        #         col1.append(x)
        #     else:
        #         continue   
    # print("~2")                                         
    return col1

if __name__ == '__main__':
    main()
    main2()
    # main3()
    # main4()
    # mainb1()
    # mainb2()