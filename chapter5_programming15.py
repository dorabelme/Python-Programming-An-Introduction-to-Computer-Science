from graphics import *

def main():

	# Open file and read it into a string
	infile = open('names_scores.txt', "r")
	n = eval(infile.readline())

	# Read in the names and scores
	names = []
	scores = []
	for i in range(n):
		name, score_str = infile.readline().split()
		names.append(name)
		scores.append(eval(score_str))

	# Create the window and set the coordinates
	win = GraphWin('Student Scores', 400, 30 * n)
	win.setCoords(-40, 0, 110, n)
	win.setBackground('white')

	# Draw in the names and rectangles
	for i in range(n):
		text = Text(Point(-20, n - 0.5 - i), names[i])
		text.setSize(10)
		text.draw(win)
		bar = Rectangle(Point(0, n - 0.7 - i), Point(scores[i], n - 0.35 - i))
		bar.draw(win)

	# Close the window and the file
	win.getMouse()
	win.close()
	infile.close()

main()

