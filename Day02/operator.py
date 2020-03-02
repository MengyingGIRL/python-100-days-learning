'''
@Time : 2020/1/6 19:13
@Author : wangmengying
@File : operator.py
'''

a = 5
b = 3
c = 10
d = 23
e = 6
a += b
a -= c
a *= d
a /= e
print("a=",a)

flag1 = 3>2
flag2 = 2<1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print('flag1 = ',flag1)
print('flag2 = ',flag2)
print('flag3 = ',flag3)
print('flag4 = ',flag4)
print('flag5 = ',flag5)
print(flag1 is True)
print(flag2 is not False)