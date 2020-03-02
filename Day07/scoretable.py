'''
输入学生考试成绩计算平均分
@Time : 2020/1/14 9:46
@Author : wangmengying
@File : scoretable.py
'''

def main():
    names = ['刘备','关羽','张飞','诸葛亮','赵云']
    subjucts = ['语文','数学','英语']
    scores = [[0]*3]*5
    for row,name in enumerate(names):
        print('请输入%s的成绩：'%name)
        for col,sub in enumerate(subjucts):
            scores[row][col] = float(input(sub + ': '))
    print(scores)

if __name__ == '__main__':
    main()