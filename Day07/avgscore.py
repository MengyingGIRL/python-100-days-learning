'''
输入学生考试成绩计算平均分
@Time : 2020/1/13 8:39
@Author : wangmengying
@File : avgscore.py
'''

def main():
    number = int(input('请输入学生人数:'))
    names = [None]*number
    scores = [None]*number
    for index in range(len(names)):
        names[index] = input('请输入第%d个学生姓名：'%(index+1))
        scores[index] = float(input(('请输入第%d个学生分数：')%(index+1)))
    total = 0
    for index in range(len(names)):
        print('%s:%.1f分'%(names[index],scores[index]))
        total += scores[index]
    print('平均分:%.2f'%(total/number))

if __name__=='__main__':
    main()