from graphics import *

def main():
	# Create the 200 by 200 pixel window
	win = GraphWin("Christmas")
	win.setBackground("white")

	# Draw the snowman
	snow_bottom = Circle(Point(60,125), 30)
	snow_bottom.draw(win)
	snow_top = Circle(Point(65,80), 20)
	snow_top.setFill("white")
	snow_top.draw(win)
	nose = Polygon(Point(75,82), Point(95, 80), Point(77,85))
	nose.setFill("orange")
	nose.draw(win)
	left_eye = Circle(Point(70,77), 2)
	left_eye.setFill("black")
	left_eye.draw(win)
	right_eye = Circle(Point(80, 76), 1.5)
	right_eye.setFill("black")
	right_eye.draw(win)
	mouth1 = Point(71, 88)
	mouth1.draw(win)
	mouth2 = Point(74, 91)
	mouth2.draw(win)
	mouth3 = Point(77, 90)
	mouth3.draw(win)
	arm = Line(Point(56, 112), Point(44, 120))
	arm.setWidth(2)
	arm.draw(win)
	forearm = Line(Point(44,120), Point(60, 130))
	forearm.draw(win)

	# Draw the tree
	bottom_tree = Polygon(Point(116,160), Point(150,110), Point(184,160))
	bottom_tree.setOutline("green")
	bottom_tree.setFill("green")
	bottom_tree.draw(win)
	mid1_tree = Polygon(Point(125,132), Point(150, 94), Point(175,132))
	mid1_tree.setOutline("green")
	mid1_tree.setFill("green")
	mid1_tree.draw(win)
	mid2_tree = Polygon(Point(132,107), Point(150, 79), Point(168,107))
	mid2_tree.setOutline("green")
	mid2_tree.setFill("green")
	mid2_tree.draw(win)
	mid2_tree = Polygon(Point(132,107), Point(150, 79), Point(168,107))
	mid2_tree.setOutline("green")
	mid2_tree.setFill("green")
	mid2_tree.draw(win)
	top_tree = Polygon(Point(138,87), Point(150, 70), Point(162,87))
	top_tree.setOutline("green")
	top_tree.setFill("green")
	top_tree.draw(win)
	ornament1 = Circle(Point(148,80), 2.5)
	ornament1.setFill("red")
	ornament1.draw(win)
	ornament2 = Circle(Point(154,97), 2.5)
	ornament2.setFill(color_rgb(153,0,204))
	ornament2.draw(win)
	ornament3 = Circle(Point(142,100), 2.5)
	ornament3.setFill(color_rgb(255,204,0))
	ornament3.draw(win)
	ornament4 = Circle(Point(155,116), 2.5)
	ornament4.setFill("red")
	ornament4.draw(win)
	ornament5 = Circle(Point(140,123), 2.5)
	ornament5.setFill(color_rgb(153,0,204))
	ornament5.draw(win)
	ornament6 = Circle(Point(160,140), 2.5)
	ornament6.setFill(color_rgb(255,204,0))
	ornament6.draw(win)
	ornament7 = Circle(Point(132,145), 2.5)
	ornament7.setFill("red")
	ornament7.draw(win)

	# Close the window on clicking the mouse
	win.getMouse()
	win.close()

main()

