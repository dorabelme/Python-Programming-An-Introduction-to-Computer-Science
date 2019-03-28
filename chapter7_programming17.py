from time import sleep
from graphics import *

def main():
	win = GraphWin("Bouncing Ball", 400, 200)
	win.setCoords(0,0,100,50)

	# Draw the ball
	ball = Circle(Point(50,25),5)
	ball.setFill("red")
	ball.draw(win)

	# Set the direction of motion initially at a 45 degree angle
	dx = 1
	dy = 1

	# Update the position every 20 ms and change the direction of motion
	# if the ball hits the wall
	for i in range(1000):
		sleep(0.02)
		ball.move(dx, dy)

		if ball.getP1().getX() == 0 or ball.getP2().getX() == 100:
			dx = -dx
		if ball.getP1().getY() == 0 or ball.getP2().getY() == 50:
			dy = -dy
	# Close the window on clicking the mouse
	win.getMouse()
	win.close()


main()

