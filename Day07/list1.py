'''
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素
@Time : 2020/1/13 9:31
@Author : wangmengying
@File : list1.py
'''

def main():
    fruits = ['orange','apple','banana','pear','strawberry']
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])
    fruits[1] = 'pineapple'
    print(fruits)
    fruits.append('watermelon')
    fruits.insert(0,'cherries')
    print(fruits)
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('pear')
    print(fruits)

if __name__ == '__main__':
    main()