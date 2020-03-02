'''
定义和使用矩形类
@Time : 2020/1/15 9:36
@Author : wangmengying
@File : react.py
'''

class React(object):
    def __init__(self,width=0,height=0):
        self._width = width
        self._height = height

    def perimeter(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._height * self._width

    def __str__(self):
        return '矩形[%f,%f]'%(self._width,self._height)

    def __del__(self):
        print('销毁矩形')

if __name__ == '__main__':
    react1 = React()
    print(react1)
    print(react1.perimeter())
    print(react1.area())
    react2 = React(3,4)
    print(react2)
    print(react2.perimeter())
    print(react2.area())