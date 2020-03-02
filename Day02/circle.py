'''
@Time : 2020/1/6 19:06
@Author : wangmengying
@File : circle.py
'''
import math

radius = float(input('请输入圆的半径：'))
permeter = 2 * math.pi * radius
area = math.pi*(radius**2)
print('周长为:%.2f'% permeter)
print('面积为:%.2f'% area)