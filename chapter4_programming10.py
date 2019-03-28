from graphics import *
from math import sqrt

def main():
	# Create the window
	win = GraphWin('Triangle Drawer', 300, 300)

	# Description
	text = Text(Point(150, 20), 'Click on three points to draw the triangle')
	text.setSize(8)
	text.draw(win)

	# Draw the rectangle
	pt1 = win.getMouse()
	pt1.draw(win)
	pt2 = win.getMouse()
	pt2.draw(win)
	pt3 = win.getMouse()
	pt1.undraw()
	pt2.undraw()
	tri = Polygon(pt1, pt2, pt3)
	tri.draw(win)

	# Calculate area and perimeter
	a = sqrt((pt2.getX() - pt1.getX())**2 + (pt2.getY() - pt1.getY())**2)
	b = sqrt((pt3.getX() - pt2.getX())**2 + (pt3.getY() - pt2.getY())**2)
	c = sqrt((pt1.getX() - pt3.getX())**2 + (pt1.getY() - pt3.getY())**2)
	s = (a+b+c) / 2
	perimeter = a + b + c
	area = sqrt(s *(s - a)*(s - b)*(s - c))


	# Display perimeter and area
	text.setText('Perimeter: ' + format(perimeter, '0.4') + ' px\nArea: ' + \
					format(area, '0.0f') + " sq px")

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()


main()
