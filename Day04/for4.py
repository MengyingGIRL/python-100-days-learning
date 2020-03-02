'''
输入一个正整数判断它是不是素数
@Time : 2020/1/8 9:40
@Author : wangmengying
@File : for4.py
'''
from math import sqrt

n = int(input('请输入一个正整数：'))
if n <= 0:
    print('wrong!')
end = int(sqrt(n))
is_prime = True
for i in range(2,end+1):
    if n % i == 0 :
        is_prime = False
        break
if is_prime and n != 0:
    print("%d 是素数" %n)
else:
    print('%d不是素数'%n)