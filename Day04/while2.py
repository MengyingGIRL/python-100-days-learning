'''
用while循环实现1~100之间的偶数求和
@Time : 2020/1/8 10:12
@Author : wangmengying
@File : while2.py
'''

num = 2
sum = 0
while num <101:
    sum += num
    num += 2
print(sum)