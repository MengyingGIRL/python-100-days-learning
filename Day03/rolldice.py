'''
@Time : 2020/1/7 9:38
@Author : wangmengying
@File : rolldice.py
'''
from random import randint

num = randint(1,6)
if num == 1:
    result = '唱首歌'
elif num == 2:
    result = '跳个舞'
elif num == 3:
    result = '学猫叫'
elif num == 4:
    result = '学狗叫'
elif num == 5:
    result = '绕口令'
else:
    result = '翻跟斗'
print(num,result)