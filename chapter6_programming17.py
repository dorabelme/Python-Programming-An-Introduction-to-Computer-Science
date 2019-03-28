from graphics import * 

def moveTo(shape, newCenter):
	oldCenter = shape.getCenter()
	dx = newCenter.getX() - oldCenter.getX()
	dy = newCenter.getY() - oldCenter.getY()
	shape.move(dx, dy)

def main():
	win = GraphWin()	
	shape = Circle(Point (50, 50), 20)
	shape.setOutline("blue")
	shape.setFill("cyan")
	shape.draw(win)
	for i in range(10):
		click_pt = win.getMouse()
		moveTo(shape, click_pt)
	win.close()

main()


