from graphics import *
from math import sqrt

def main():
	# Create the window and set useful coordinates
	win = GraphWin('Circle Intersection Calculator', 300, 330)
	win.setCoords(-10, -12, 10, 10)

	# Screen 1: Description
	descr = Text(Point(0,0), 'This program calculates the\n' +
							'x values of the intersection of a\n' +
							'horizontal line and circle.')
	click = Text(Point(0, -11), 'Click anywhere to continue.')
	descr.setSize(8)
	click.setSize(8)
	descr.draw(win)
	click.draw(win)

	# Wait for mouse click and then clear screen
	win.getMouse()
	descr.undraw()

	# Screen 2: Obtainingg input from the user
	# Add entry boxes for radius and y-intercept
	rad_text = Text(Point(-5,5), 'Radius: ')
	int_text = Text(Point(-5,0), 'Intercept: ')
	rad_text.setSize(8)
	int_text.setSize(8)
	rad_text.draw(win)
	int_text.draw(win)
	rad_input = Entry(Point(0,5), 3)
	int_input = Entry(Point(0,0), 3)
	rad_input.setSize(8)
	int_input.setSize(8)
	rad_input.draw(win)
	int_input.draw(win)

	# Get radius and intercept from user and clear screen
	win.getMouse()
	radius = eval(rad_input.getText())
	intercept = eval(int_input.getText())
	rad_text.undraw()
	int_text.undraw()
	rad_input.undraw()
	int_input.undraw()
	click.undraw()

	# Compute x values of intersection
	if abs(intercept) <= radius:
	x_int1 = - sqrt(radius ** 2 - intercept ** 2)
	x_int2 = sqrt(radius ** 2 - intercept ** 2)

	# Screen 3: Displaying data
	# Draw circle and line on x and y axes
	x_axis = Line(Point(-10,0), Point(10,0))
	x_axis.setArrow('last')
	y_axis = Line(Point(0,-10), Point(0,10))
	y_axis.setArrow('last')
	circ = Circle(Point(0,0), radius)
	circ.setOutline('blue')
	line = Line(Point(-10, intercept), Point(10, intercept))
	line.setOutline('blue')
	x_axis.draw(win)
	y_axis.draw(win)
	circ.draw(win)
	line.draw(win)

	if abs(intercept) <= radius:
		int1 = Circle(Point(x_int1, intercept), 0.2)
		int1.setFill('red')
		int1.setOutline('red')
		int2 = Circle(Point(x_int2, intercept), 0.2)
		int2.setFill('red')
		int2.setOutline('red')
		int1.draw(win)
		int2.draw(win)

	# Display data
	if abs(intercept) <= radius:
		int_info = Text(Point(0,-11), 'x values of points of intersection: ' +
									str(x_int1) + ', ' + str(x_int2))

	elif abs(intercept) == radius:
		int_info = Text(Point(0,-11), 'x value of point of intersection: 0.0')

	else:
		int_info = Text(Point(0,-11), 'There are no points of intersection.')
									
	int_info.setSize(8)
	int_info.draw(win)

	# CLose the window on clicking the mouse
	win.getMouse()
	win.close()


main()

