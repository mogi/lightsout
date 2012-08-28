#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lightsout

作ってからCellにreverseメソッドをもたせた方が
オートマトンとして振舞わせることができて応用が効くことに気づいた。
たぶん出題者の意図からしてもCellに振る舞いをもたせるのが正解だったぽい
"""

class Cell():
    FACE = 1
    BACK = 2
    SYMBOL = {1:"-", 2:"x"}
    def __init__(self):
        self._state = self.FACE

    @property
    def state(self):
        return self.SYMBOL[self._state]

    def is_face(self):
        return self._state == self.FACE

    def is_back(self):
        return self._state == self.BACK

    def reverse(self):
        if self.is_face():
            self._state = self.BACK
        elif self.is_back():
            self._state = self.FACE


class Board():
    HIGHT = 4
    WIDTH = 4
    def __init__(self):
        self.cells = self._create(self.HIGHT, self.WIDTH)

    def _create(self, hight=4, width=4):
        cells = {}
        for i in range(hight):
            for j in range(width):
                key = self.key_gen(i,j)
                cells[key] = Cell()
        return cells

    @classmethod
    def key_gen(cls, hight, width):
        return str(hight) + "," + str(width)


class GameManeger():
    def __init__(self):
        self.board = Board()
        self.out()

    def execute(self, _hight, _width):
        hight = int(_hight)-1
        width = int(_width)-1
        self.reverse(hight, width)
        self.out()
        return self.is_finish()

    def _reverse(self, hight, width):
        key = Board.key_gen(hight, width)
        if self.board.cells.has_key(key):
            self.board.cells[key].reverse()

    def reverse(self, hight, width):
        # center
        self._reverse(hight, width)
        # left
        self._reverse(hight, width-1)
        # right
        self._reverse(hight, width+1)
        # top
        self._reverse(hight-1, width)
        # bottom
        self._reverse(hight+1, width)

    def out(self):
        line = u"  "
        for i in range(self.board.WIDTH):
            line = line + str(i+1) + " "
        else:
            print line
        for hight in range(self.board.HIGHT):
            line = str(hight+1) + " "
            for width in range(self.board.WIDTH):
                key = Board.key_gen(hight, width)
                line = line + str(self.board.cells[key].state) + " "
            else:
                print line

    def is_finish(self):
        for cell in self.board.cells.values():
            if cell.is_face():
                return False
        else:
            return True


if __name__ == '__main__':
    gm = GameManeger()

    fin = False
    while fin != True:
        print "hight->"
        raw1 = raw_input()
        print "width->"
        raw2 = raw_input()
        fin = gm.execute(raw1, raw2)
    print "Finish"
