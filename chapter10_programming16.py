# Problem 16

from projectile import Projectile
from tracker import Tracker
from graphics import *
from time import sleep
sleep(0.005)
from target import Target


def main ():

    #Introduction
    print ("This program uses a cannonball to shoot at a target.")

    #Create graphics window
    win = GraphWin("Target", 200, 200)
    win.setCoords(0.0, 0.0, 25.0, 25.0)
    target = Target(win)

    flag = False
    targetHit = False
    while not flag:

    #Get inputs
        print ()
        a = eval(input("Enter the launch angle in degrees: "))
        v = eval(input("Enter the initial velocity in meters per second: "))
        h = eval(input("Enter the initial height in meters: "))

    #Create tracker
        projectile = Projectile(a, v, h)
        tracker = Tracker(win, projectile)
        time = 0.0
        while projectile.getY() >= -5:
            time += .0005
            projectile.update(time)
            tracker.update()

    #Calculate if cannonball hit target
            points = target.points()
            center = tracker.circ.getCenter()
            center_x = center.getX()
            center_y = center.getY()
            radius = tracker.circ.getRadius()
            for point in points:
                x = point.getX()
                y = point.getY()
                square_dist = (center_x-x) ** 2 + (center_y-y) ** 2
                if square_dist <= radius ** 2:
                    targetHit = True
        if targetHit:
            print ("\nYou hit the target!")
            flag = True
        else:
            flag = False
            print ("\nTry again!")


    #Close window
    win.getMouse()
    win.close()






if __name__ == '__main__':
    main ()