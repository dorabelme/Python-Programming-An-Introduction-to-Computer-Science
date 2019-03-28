from graphics import *


def main():
	# Create the 200 by 200 pixel window
	win = GraphWin("Self-Portrait")
	win.setBackground("white")

	# Draw the face
	outline = Circle(Point(100,100), 50)
	outline.draw(win)
	left_eye = Circle(Point(77,80), 5)
	left_eye.setFill("black")
	left_eye.draw(win)
	right_eye = Circle(Point(123,80), 5)
	right_eye.setFill("black")
	right_eye.draw(win)
	nose = Line(Point(100,90), Point(100,110))
	nose.draw(win)
	mouth = Polygon(Point(70,120), Point(130,120), Point(115,130))
	mouth.setFill("black")
	mouth.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()


