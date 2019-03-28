from graphics import *

def main():
	# Introduction
	print("This program plots the growth of a 10-year investment.")

	# Create a graphics window with labels on left edge
	win = GraphWin("Investment Growth Chart", 640, 480)
	win.setBackground("white")
	win.setCoords(-1.75, -200, 11.5, 14000)
	Text(Point(-1, 0), ' 0.0K').draw(win)
	Text(Point(-1, 2500), ' 2.5K').draw(win)
	Text(Point(-1, 5000), ' 5.0K').draw(win)
	Text(Point(-1, 7500), ' 7.5K').draw(win)
	Text(Point(-1, 10000), ' 10.0K').draw(win)


	# Create the principal and apr Entry objects along with some Text
	Text(Point(0,12500), 'Principal: ').draw(win)
	Text(Point(7,12500), 'APR: ').draw(win)
	print_input = Entry(Point(3.5, 12500), 10).draw(win)
	apr_input = Entry(Point(9, 12500), 5).draw(win)

	# Wait for a mouse click
	win.getMouse()

	# Conversions
	principal = eval(print_input.getText())
	apr = eval(apr_input.getText())

	# Draw bar for initial principal
	bar = Rectangle(Point(0,0), Point(1, principal))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	# Draw a bar for each subsequent year
	for year in range(1,11):
		principal = principal * (1 + apr)
		bar = Rectangle(Point(year, 0), Point(year + 1, principal))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	input("Press <Enter> to quit.")
	win.close()

main()

