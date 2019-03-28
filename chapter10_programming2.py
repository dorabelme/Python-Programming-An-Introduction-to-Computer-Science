""" using Chapter 8, Programming Exercise 13"""

from graphics import *
from button import Button

def main():
	# Create the window and set useful coordinates
	win = GraphWin("Regression Line Example", 300, 330)
	win.setCoords(-10,-12,10,10)

	# Screen 1: Description
	descr = Text(Point(0,0), 'This program calculates and draws\n' + \
							'the regression line for a sequence\n' +\
							'of points in the plane.')
	bot_text = Text(Point(0,-11), 'Click anywhere to continue.')
	descr.setSize(8)
	bot_text.setSize(8)
	descr.draw(win)
	bot_text.draw(win)

	# Wait for the mouse click and then clear screen
	win.getMouse()
	descr.undraw()

	# Screen 2: Graph
	bot_text.setText('Click on the graph to add points.')
	x_axis = Line(Point(-10,0), Point(10,0))
	x_axis.setArrow('last')
	y_axis = Line(Point(0,-10), Point(0,10))
	y_axis.setArrow('last')
	x_axis.draw(win)
	y_axis.draw(win)
	done = Button(win, Point(-7.75, -11), 3.5, 1, "Done")

	# Get points
	x_coords = []
	y_coords = []
	click = win.getMouse()
	counter = 1
	while not done.clicked(click):
		click.draw(win)
		x_coords.append(click.getX())
		y_coords.append(click.getY())
		counter += 1
		if counter == 3:
			done.activate()
		click = win.getMouse()

	# Calculation
	n = len(x_coords)
	if n > 0:
		x_bar = sum(x_coords) / n
		y_bar = sum(y_coords) / n
		numerator = -n * x_bar * y_bar
		denominator = -n * x_bar ** 2
		for i in range(n):
			numerator += x_coords[i] * y_coords[i]
			denominator += x_coords[i] ** 2
		m = numerator / denominator
		left_y = y_bar + m * (-10 - x_bar)
		right_y = y_bar + m * (10 - x_bar)

	# Screen 3: Regression Line
	bot_text.undraw()
	done.deactivate()
	if n > 0:
		reg_line = Line(Point(-10, left_y), Point(10, right_y))
		reg_line.setOutline('red')
		reg_line.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()


