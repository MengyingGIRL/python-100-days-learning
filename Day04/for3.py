'''
输入非负整数n计算n!
@Time : 2020/1/8 9:21
@Author : wangmengying
@File : for3.py
'''
n = int(input('请输入非负整数：'))
if n <= 0:
    print('输入错误！')
result = 1
for i in range(1,n+1):
    result *= i
print(result)