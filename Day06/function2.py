'''
函数的定义和使用 - 求最大公约数和最小公倍数
@Time : 2020/1/10 14:08
@Author : wangmengying
@File : function2.py
'''

def gcd(x,y):
    if x > y:
        x,y = y,x
    for i in range(x,0,-1):
        if x % i == 0 and y % i == 0:
            return i
    return 1

def lcm(x,y):
    return (x * y // gcd(x,y))

print(gcd(7,14))
print(lcm(76,24))