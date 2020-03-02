'''
双色球随机选号程序
@Time : 2020/1/14 8:50
@Author : wangmengying
@File : lottery.py
'''
from random import randint,sample

def display(balls):
    """
    输出列表中的双色球号码
    """
    for index,ball in enumerate(balls):
        if index == len(balls)-1:
            print('|',end=' ')
        print('%02d'%ball,end=' ')
    print()

def random_select():
    red_balls = [x for x in range(1,34)]
    selected_balls = sample(red_balls,6)
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()
