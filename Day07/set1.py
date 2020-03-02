'''
定义和使用集合
@Time : 2020/1/14 9:52
@Author : wangmengying
@File : set1.py
'''

def main():
    set1 = {1,2,3,4,5,3,2}
    print(set1)
    print(len(set1))
    set2 = set(range(1,10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11,12])
    print(set1)
    print(set2)
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    for elem in set2:
        print(elem,end=' ')
    print()
    set3 = set((1,2,3,3,2,1))
    print(set3.pop())
    print(set3)

if __name__ == '__main__':
    main()
