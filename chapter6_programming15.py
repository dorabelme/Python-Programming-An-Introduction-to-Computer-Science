from graphics import *

def drawFace(center, size, win):
	# Draw outline
	outline = Circle(center,size)
	outline.draw(win)
	
	# Draw eyes
	lt_eye_pt = center.clone()
	lt_eye_pt.move(-size / 2, size / 3)
	left_eye = Circle(lt_eye_pt, size / 10)
	left_eye.setFill("black")
	left_eye.draw(win)
	rt_eye_pt = center.clone()
	rt_eye_pt.move(size / 2, size / 3)
	right_eye = Circle(rt_eye_pt, size / 10)
	right_eye.setFill("black")
	right_eye.draw(win)
	
	# Draw nose
	nose = Line(Point(center.getX(), center.getY() - size / 7.5), \
				Point(center.getX(), center.getY() + size / 10))
	nose.draw(win)
				
	# Draw mouth
	mouth = Polygon(Point(center.getX() - size / 2, center.getX() - 2 * size / 5),
				Point(center.getX() + size / 2, center.getX() - 2 * size / 5),
				Point(center.getX() + 3 * size / 10, center.getX() - 3 * size / 5))
	mouth.setFill("black")
	mouth.draw(win)
	
def main():
	win = GraphWin("Faces", 400, 400)
	win.setCoords(0,0,100,100)
	win.setBackground("white")

	drawFace(Point(50,50), 10, win)
	drawFace(Point(10,10), 5, win)
	drawFace(Point(87,87), 20, win)

	win.getMouse()
	win.close()

main()

