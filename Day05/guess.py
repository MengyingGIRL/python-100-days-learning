'''
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
@Time : 2020/1/9 10:38
@Author : wangmengying
@File : guess.py
'''
from random import randint

num = randint(1,101)
count = 0
while True:
    count += 1
    x = int(input('请猜数字：'))
    if x > num:
        print('小一点')
    elif x < num:
        print('大一点')
    else:
        print('猜对了！')
        break
print(count)