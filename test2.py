from random import randint
y = [[x for x in range(10)],[x for x in range(10)]]
i = [x for x in range(10)]
# x = [4,5,6,1,3,1,4,5]
print(i)
m = 1
st1 = [x for x in i if x % 2 == 0 and m > 4]
print(st1)
# for x in st1:
#     print(x)