'''
@Time : 2020/1/7 8:48
@Author : wangmengying
@File : conversion.py
'''

value = float(input('请输入数字: '))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.2f 英寸 = %.2f 厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f 厘米 = %.2f 英寸'% (value, value / 2.54))
else:
    print('请输入有效单位！')