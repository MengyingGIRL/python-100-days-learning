'''
斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
@Time : 2020/1/9 10:26
@Author : wangmengying
@File : Fibonacci.py
'''

x = 0
y = 1
for _ in range(20):
    x,y = y,x+y
    print(x)