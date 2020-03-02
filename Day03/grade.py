'''
@Time : 2020/1/7 9:16
@Author : wangmengying
@File : grade.py
'''

score = float(input('请输入分数:'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('分数为:%f,等级为：%s'%(score,grade))