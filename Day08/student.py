'''
定义和使用学生类
@Time : 2020/1/15 9:42
@Author : wangmengying
@File : student.py
'''

def _foo():
    print('test')

class Student(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def study(self,course_name):
        print('%s正在学习%s'%(self._name,course_name))

    def watch_mv(self):
        if self._age< 18:
            print('%s只能看熊出没'%self._name)
        else:
            print('%s可以看全部电影'%self._name)

def main():
    stu1 = Student('wmy',19)
    stu1.study('english')
    stu1.watch_mv()

if __name__ == '__main__':
    main()