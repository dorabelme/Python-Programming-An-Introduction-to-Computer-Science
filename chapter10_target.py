# target.py

from graphics import *
from random import randrange

class Target:

    def __init__(self,win):
        x1 = randrange(1, 15)
        x2 = 5
        x2 = x1 + x2
        self.rect = Rectangle(Point(x1, 2),Point(x2, 4))
        self.rect.draw(win)
        label = Text(Point(x1 + 2, 3), "Target")
        label.draw(win)

    def points(self):
        points = []
        p1 = self.rect.getP1()
        x1 = p1.getX()
        p2 = self.rect.getP2()
        x2 = p2.getX()
        for x in range(x1, x2 + 1):
            for y in range(2, 5):
                point = Point(x,y)
                points.append(point)
        return points
