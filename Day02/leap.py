'''
@Time : 2020/1/6 19:09
@Author : wangmengying
@File : leap.py
'''

year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(is_leap)