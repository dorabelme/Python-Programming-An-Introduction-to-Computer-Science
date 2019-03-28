from graphics import *
from math import sqrt

def main():
	# Create the window
	win = GraphWin('Rectangle Drawer', 300, 300)

	# Description
	text = Text(Point(150, 20), 'Click on two points to draw the rectangle')
	text.setSize(8)
	text.draw(win)

	# Draw the rectangle
	pt1 = win.getMouse()
	pt1.draw(win)
	pt2 = win.getMouse()
	pt2.draw(win)
	line = Rectangle(pt1, pt2)
	line.draw(win)

	# Calculate the area and perimeter
	length = abs(pt2.getY() - pt1.getY())
	width = abs(pt2.getX() - pt1.getX())
	area = length * width
	perimeter = 2 * (length + width)

	# Display perimeter and area
	text.setText('Perimeter: ' + format(perimeter, '0.4') + ' px\nArea: ' + \
					format(area, '0.0f') + " sq px")

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()


main()
