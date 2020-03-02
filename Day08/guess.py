'''
面向对象版本的猜数字游戏
@Time : 2020/1/15 8:45
@Author : wangmengying
@File : guess.py
'''
from random import randint

class GuessMachine(object):
    def __init__(self):
        self._answer = None
        self._counter = None
        self._hint = None

    def reset(self):
        self._answer = randint(1,100)
        self._counter = 0
        self._hint = None

    def guess(self,your_answer):
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '猜小一点'
        elif your_answer < self._answer:
            self._hint = '猜大一点'
        else:
            self._hint = '恭喜你，猜对了！'
            return True
        return False

    @property
    def counter(self):
        return self._counter

    @property
    def hint(self):
        return self._hint

if __name__ == '__main__':
    gm = GuessMachine()
    play = True
    while play:
        game_over = False
        gm.reset()
        while not game_over:
            your_answer = int(input('请输入你猜的数字:'))
            game_over = gm.guess(your_answer)
            print(gm.hint)
        if gm.counter > 7:
            print('你的智商余额不足')
        play = input('go on|yes or no?') == 'yes'