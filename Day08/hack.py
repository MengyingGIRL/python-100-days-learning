'''
另一种创建类的方式
@Time : 2020/1/15 9:30
@Author : wangmengying
@File : hack.py
'''

def bar(self,name):
    self._name = name

def foo(self,course_name):
    print('%s正在学习%s'%(self._name,course_name))

def main():
    Student = type('Student',(object,),dict(__init__ = bar,study = foo))
    stu1 = Student('wmy')
    stu1.study('Python')

if __name__ == '__main__':
    main()