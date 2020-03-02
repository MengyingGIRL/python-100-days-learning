'''
输入学生考试成绩计算平均分
@Time : 2020/1/14 9:42
@Author : wangmengying
@File : marquee.py
'''
import os
import time

def main():
    str = 'welcome to Beijing    '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:]+str[0:1]
        os.system('clear')

if __name__ == '__main__':
    main()
