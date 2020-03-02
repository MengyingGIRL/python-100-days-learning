'''
作用域问题
@Time : 2020/1/10 14:46
@Author : wangmengying
@File : function6.py
'''

def foo1():
    a=3

print(foo1())

b=2

def foo2():
    print(b)

foo2()

def foo3():
    b=100
    print(b)

foo3()
print(b)

def foo4():
    global b
    b=700
    print(b)

foo4()
print(b)