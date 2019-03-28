from graphics import *
from math import sqrt

def main():
	# Create the window
	win = GraphWin('House Drawer', 300, 300)

	# Description
	text = Text(Point(150, 20), 'It takes 5 clicks to build a house\n' +
								 'First build the walls')
	text.setSize(8)
	text.draw(win)

	# Draw the outline
	pt1 = win.getMouse()
	pt1.draw(win)
	pt2 = win.getMouse()
	pt1.undraw()
	walls = Rectangle(pt1, pt2)
	walls.draw(win)

	# Figure out which corners are which and calculate the width of the house
	ul_corner = Point(min(pt1.getX(), pt2.getX()), min(pt1.getY(), pt2.getY()))
	ur_corner = Point(max(pt1.getX(), pt2.getX()), min(pt1.getY(), pt2.getY()))
	ll_corner = Point(min(pt1.getX(), pt2.getX()), max(pt1.getY(), pt2.getY()))
	lr_corner = Point(max(pt1.getX(), pt2.getX()), max(pt1.getY(), pt2.getY()))
	width = ur_corner.getX() - ul_corner.getX()

	# Draw the door
	text.setText('It takes 5 clicks to build a house\n' +
				'Now add the door')
	pt3 = win.getMouse()
	ul_door = pt3.clone()
	ul_door.move(-width / 10, 0)
	door = Rectangle(ul_door, Point(pt3.getX() + width / 10, ll_corner.getY()))
	door.draw(win)

	# Draw the window
	text.setText('It takes 5 clicks to build a house\n' +
				'Now we need a window')
	pt4 = win.getMouse()
	ul_window = pt4.clone()
	ul_window.move(-width / 20, -width / 20)
	lr_window = pt4.clone()
	lr_window.move(width / 20, width / 20)
	window = Rectangle(ul_window, lr_window)
	window.draw(win)

	# Draw the roof
	text.setText('It takes 5 clicks to build a house\n' +
				'Finally, we need a roof for this house')
	pt5 = win.getMouse()
	roof = Polygon(pt5, ul_corner, ur_corner)
	roof.draw(win)

	# Remove the text at the top
	text.undraw()

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()



main()

