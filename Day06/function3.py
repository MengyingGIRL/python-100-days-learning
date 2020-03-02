'''
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type
@Time : 2020/1/10 14:15
@Author : wangmengying
@File : function3.py
'''

def myfilter(mystr):
    return len(mystr)==6

print(chr(0x9a8f))
print(hex(ord('王')))
print(abs(-3.14156))
print(round(-3.14156))
print(pow(3.14156,5))
fruits = ['orange','apple','strawberry','banana','pear']
print(fruits[slice(1,3)])
fruits1 = list(filter(myfilter,fruits))
print(fruits)
print(fruits1)