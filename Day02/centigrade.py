'''
@Time : 2020/1/6 19:03
@Author : wangmengying
@File : centigrade.py
'''

f = float(input('请输入华氏温度:'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度'%(f, c))