from graphics import *
from math import sqrt

def main():
	# Create the window
	win = GraphWin('Line Segment Drawer', 300, 300)

	# Description
	text = Text(Point(150, 20), 'Click on two points to draw the line segment')
	text.setSize(8)
	text.draw(win)

	# Draw the line segment
	pt1 = win.getMouse()
	pt1.draw(win)
	pt2 = win.getMouse()
	pt2.draw(win)
	line = Line(pt1, pt2)
	line.setWidth(2)
	line.draw(win)

	# Calculate and draw midpoint
	mid_x = (pt1.getX() + pt2.getX()) / 2
	mid_y = (pt1.getY() + pt2.getY()) / 2
	midpt = Circle(Point(mid_x, mid_y), 2)
	midpt.setOutline('red')
	midpt.setFill('red')
	midpt.draw(win)

	# Display the length and the slope
	dx = pt2.getX() - pt1.getX()
	dy = pt2.getY() - pt1.getY()
	slope = - dy / dx
	length = sqrt(dx ** 2 + dy ** 2)
	text.setText('Slope: ' + format(slope, '0.4') + '\nLength: ' + \
					format(length, '0.4') + " px")

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()


main()
