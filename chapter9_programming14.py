# get the number of steps from the user, num_steps
# create a GraphWin window and set useful coordinates
# draw the x and y axes
# initialize x and y to 0
# loop num_steps times
	# generate a random angle
	# set x1 to x + cos(angle)
	# set y1 to y + sin(angle)
	# draw a line segment from (x,y) to (x1,y1)
	# set x to x1 and y to y1
# close window on click


import math
from random import random
from graphics import *

def main():
	num_steps = eval(input("Enter the number of steps to take: "))
	
	# Create window
	win = GraphWin("2D Random Walk", 300, 300)
	win.setCoords(-50, -50, 50, 50)

	# Draw axes
	x_axis = Line(Point(-50, 0), Point(50, 0))
	x_axis.setArrow("last")
	y_axis = Line(Point(0, -50), Point(0, 50))
	y_axis.setArrow("last")
	x_axis.draw(win)
	y_axis.draw(win)

	# Draw random walk
	x = 0
	y = 0
	for j in range(num_steps):
		angle = random() * 2 * math.pi
		x1 = x + math.cos(angle)
		y1 = y + math.sin(angle)
		step = Line(Point(x,y), Point(x1,y1))
		step.setOutline("red")
		step.draw(win)
		x = x1
		y = y1

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()
