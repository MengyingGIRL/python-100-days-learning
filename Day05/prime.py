'''
输出2~99之间的素数
@Time : 2020/1/9 10:34
@Author : wangmengying
@File : prime.py
'''
import math

for num in range(2,99):
    is_prime = True
    for factor in range(2,int(math.sqrt(num))+1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)