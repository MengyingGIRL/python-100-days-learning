'''
找出列表中最大或最小的元素
@Time : 2020/1/13 9:24
@Author : wangmengying
@File : findmax.py
'''

def main():
    fruits = ['orange','apple','banana','pear','strawberry']
    max_value = min_value = fruits[0]
    for index in range(1,len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print(max_value)
    print(min_value)

if __name__ == '__main__':
    main()