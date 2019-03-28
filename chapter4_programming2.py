from graphics import *


def main():
	# Create the 200 by 200 pixel window
	win = GraphWin("Target")

	# Draw in each of the circles
	white_circle = Circle(Point(100,100), 50)
	white_circle.setFill("white")
	white_circle.draw(win)

	black_circle = Circle(Point(100,100), 40)
	black_circle.setFill("black")
	black_circle.draw(win)

	blue_circle = Circle(Point(100,100), 30)
	blue_circle.setFill("blue")
	blue_circle.draw(win)

	red_circle = Circle(Point(100,100), 20)
	red_circle.setFill("red")
	red_circle.draw(win)	

	yellow_circle = Circle(Point(100,100), 10)
	yellow_circle.setFill("yellow")
	yellow_circle.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()

