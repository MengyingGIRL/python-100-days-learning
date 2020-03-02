'''
正整数的反转
@Time : 2020/1/9 10:06
@Author : wangmengying
@File : palindrome.py
'''

num = int(input('请输入一个正整数：'))
reversed_num = 0
while num > 0:
    reversed_num = num % 10 + reversed_num * 10
    num = num // 10
print(reversed_num)