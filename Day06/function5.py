'''
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
@Time : 2020/1/10 14:32
@Author : wangmengying
@File : function5.py
'''
# 参数默认值
def f1(a,b=1,c=5):
    return (a + b*2 + c*3)

print(f1(1,5,6))
print(f1(2,3))
print(f1(2))
print(f1(c=12,a=23,b=1))

# 可变参数
def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(f2(2,2,3))
print(f2(3,5))
print(f2(1,2,3))
print(f2())

# 关键字参数
def f3(**kw):
    if 'name' in kw:
        print(kw['name'])
    elif 'tel' in kw:
        print(kw['tel'])
    else:
        print('none')

params = {'name':'mengying','age':25}
f3(**params)
f3(name='mengying',tel='1234567890')
f3(user='mengying',age=23,tel=1234567890)

