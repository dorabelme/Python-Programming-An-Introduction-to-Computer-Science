from graphics import *

class Tracker:

    def __init__(self, window, objToTrack):

        # window is a graphWin and objToTrack is an object whose
        #  position is to be shown in the window. objToTrack is
        #  an object that has getX() and getY() methods that
        #  report its current position.

        # Creates a Tracker object and draws a circle in window
        #   at the current position of objToTrack.

        self.objToTrack = objToTrack
        self.circ = Circle(Point(objToTrack.getX(), objToTrack.getY()), 2)
        self.circ.draw(window)

    def update(self):
        point = self.circ.getCenter()
        x = point.getX()
        y = point.getY()
        self.circ.move(self.objToTrack.getX() - x, self.objToTrack.getY() - y)
