'''
定义和使用字典
@Time : 2020/1/13 8:50
@Author : wangmengying
@File : dict1.py
'''

def main():
    scores = {'狄仁杰':92,'白元芳':89,'李元芳':90}
    print(scores['狄仁杰'])
    print(scores['白元芳'])
    for elem in scores:
        print('%s\t--->\t%d' % (elem,scores[elem]))
    scores['白元芳'] = 78
    scores['诸葛亮'] = 100
    scores.update(方培=67,方琦=94)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.get('武则天',100))
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('李元芳',80))
    scores.clear()
    print(scores)

if __name__ == '__main__':
    main()