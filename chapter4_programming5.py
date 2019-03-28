from graphics import *

def main():
	# Create the 400 by 100 pixel window
	win = GraphWin('Dice Straight', 400, 100)
	win.setCoords(0,0,16,4)

	# Draw the die outlines
	for i in range(4):
		die = Rectangle(Point(1 + i * 3, 3), Point(3 + i * 3, 1))
		die.setFill('white')
		die.draw(win)

	# Draw upper left corner dots
	for i in range(4):
		circ = Circle(Point(1.3 + i * 3, 2.7), 0.1)
		circ.setFill('black')
		circ.draw(win)

	# Draw lower right corner dots
	for i in range(4):
		circ = Circle(Point(2.7 + i * 3, 1.3), 0.1)
		circ.setFill('black')
		circ.draw(win)

	# Draw middle dots
	for i in range(2):
		circ = Circle(Point(5 + i * 6, 2), 0.1)
		circ.setFill('black')
		circ.draw(win)

	# Draw upper right corner dots
	for i in range(2):
		circ = Circle(Point(8.7 + i * 3, 2.7), 0.1)
		circ.setFill('black')
		circ.draw(win)

	# Draw lower left corner dots
	for i in range(2):
		circ = Circle(Point(7.3 + i * 3, 1.3), 0.1)
		circ.setFill('black')
		circ.draw(win)

	# Draw die 6
	die6 = Rectangle(Point(13,3), Point(15,1))
	die6.setFill('black')
	die6.draw(win)
	circ1 = Circle(Point(13.3, 2.7), 0.1)
	circ1.setFill('white')
	circ1.setOutline('white')
	circ1.draw(win)
	for i in range(1,3):
		circ = circ1.clone()
		circ.move(0, -i*0.7)
		circ.draw(win)
	for i in range(3):
		circ = circ1.clone()
		circ.move(1.4, -i*0.7)
		circ.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()

