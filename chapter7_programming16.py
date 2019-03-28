from math import sqrt
from graphics import *


def main():
	# Create the 200 by 200 pixel window
	win = GraphWin("Arrow Game", 400, 440)
	win.setCoords(0,0,100,110)

	# Draw in each of the circles
	white_circle = Circle(Point(50,60), 25)
	white_circle.setFill("white")
	white_circle.draw(win)

	black_circle = Circle(Point(50,60), 20)
	black_circle.setFill("black")
	black_circle.draw(win)

	blue_circle = Circle(Point(50,60), 15)
	blue_circle.setFill("blue")
	blue_circle.draw(win)

	red_circle = Circle(Point(50,60), 10)
	red_circle.setFill("red")
	red_circle.draw(win)	

	yellow_circle = Circle(Point(50,60), 5)
	yellow_circle.setFill("yellow")
	yellow_circle.draw(win)

	# Display initial message
	msg = Text(Point(50, 5), "Fire 5 more arrows")
	msg.setSize(10)
	msg.draw(win)

	# Fire the shots and update the message including the score
	score = 0
	for i in range(4,-1,-1):
		shot = win.getMouse()
		arrow = Circle(shot, 1)
		arrow.setFill("orange")
		arrow.setOutline("orange")
		arrow.draw(win)
		distance = sqrt((50 - shot.getX()) ** 2 + (60 - shot.getY())** 2)
		if distance <= 25:
			score += round(9 - 2 * (distance // 5))
		if i > 1:
			msg.setText("Fire " + str(i) + " more arrows\n" + \
				"Score: " + str(score))
		elif i == 1:
			msg.setText("Fire your last arrow\n" + \
				"Score: " + str(score))
		else:
			msg.setText("Score: " + str(score))

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()

