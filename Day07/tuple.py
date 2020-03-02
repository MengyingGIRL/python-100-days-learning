'''
元组的定义和使用
@Time : 2020/1/14 10:11
@Author : wangmengying
@File : tuple.py
'''

def main():
    t = ('wmy',25,'yichang',False)
    print(t)
    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])
    for memeber in t:
        print(memeber)
    t = ('amy',16,True,'Beijing')
    print(t)
    person = list(t)
    print(person)
    person[0] = 'kate'
    person[1] = 18
    print(person)
    fruits_list = ['apple','banana','pear']
    fruits_t = tuple(fruits_list)
    print(fruits_t)
    print(fruits_t[0])


if __name__ == '__main__':
    main()