'''
定义和使用时钟类
@Time : 2020/1/14 10:41
@Author : wangmengying
@File : clock.py
'''
import os
import time

class Clock(object):
    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self,**kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        print('%02d:%02d:%02d' % (self._hour,self._minute,self._second))

if __name__ == '__main__':
    clock = Clock()
    while True:
        os.system('cls')
        print(clock.show())
        time.sleep(1)
        clock.run()