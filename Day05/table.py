'''
输出乘法口诀表(九九表)
@Time : 2020/1/9 10:42
@Author : wangmengying
@File : table.py
'''

for i in range(1,10):
    for j in range(1,i+1):
        print('%d * %d = %d'%(i,j,i*j),end='\t')
    print()