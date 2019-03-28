from projectile import Projectile
from tracker import Tracker
from graphics import *
from time import sleep
sleep(0.005)



def main ():

    #Introduction
    print ("This program graphically depicts the flight of a cannonball. ")
    print ()

    #Get inputs
    a = eval(input("Enter the launch angle in degrees: "))
    v = eval(input("Enter the initial velocity in meters per second: "))
    h = eval(input("Enter the initial height in meters: "))

    #Create tracker
    projectile = Projectile(a, v, h)
    win = GraphWin("Tracker", 600, 600)
    win.setCoords(0.0, 0.0, 25.0, 25.0)
    tracker = Tracker(win, projectile)
    time = 0.0
    while projectile.getY() >= -5:
        time += .0005
        projectile.update(time)
        tracker.update()

    #Close window
    win.getMouse()
    win.close()






if __name__ == '__main__':
    main ()