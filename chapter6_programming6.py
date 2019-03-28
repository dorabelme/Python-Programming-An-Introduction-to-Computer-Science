# Program calculates the area of a triangle
# Input 3 sides

import math
from graphics import *

def square(x):
	return x * x

def distance(p1,p2):
	dist = math.sqrt(square(p2.getX() - p1.getX()) + \
						square(p2.getY() - p1.getY()))
	return dist

def area(side1, side2, side3):
	s = (side1 + side2 + side3) / 2
	A = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
	return A


def main():
	win = GraphWin("Draw a Triangle")
	win.setCoords(0.0, 0.0, 10.0, 10.0)
	message = Text(Point(5, 1), "Click on three points")
	message.setSize(10)
	message.draw(win)

	# Get and draw three vertices of traingle
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)

	# Use Polygon object to draw the triangle
	triangle = Polygon(p1, p2, p3)
	triangle.setFill("peachpuff")
	triangle.setOutline("cyan")
	triangle.draw(win)

	# Calculate the side lenght
	a = distance(p1, p2)
	b = distance(p2, p3)
	c = distance(p3, p1)

	# Calculate the perimeter and area of the triangle
	perimeter = a + b + c
	ar = area(a,b,c)
	message.setText(("The perimeter is: {0:0.2f}\nThe area is: " +\
						"{1:0.2f}".format(perimeter, ar))

	# Wait for another click to exit
	win.getMouse()
	win.close()

main()




