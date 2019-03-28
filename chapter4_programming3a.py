from graphics import *


def main():
	# Create tthe face and two eyes
	win = GraphWin("Face")

	# Draw in each of the circles
	face = Circle(Point(100,100), 50)
	face.draw(win)

	left_eye = Circle(Point(80,80), 10)
	left_eye.setFill("black")
	left_eye.draw(win)
	right_eye = Circle(Point(120,80), 10)
	right_eye.setFill("black")
	right_eye.draw(win)
	mouth = Line(Point(75, 130), Point(125, 130))
	mouth.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()


