from graphics import *

def main():

	# Open file 
	infile = open('0-10_count.txt', "r")

	# Create list of numbers from file
	num_str = infile.readlines()
	count_list = [0] * 11
	for num in num_str:
		count_list[eval(num)] += 1


	# Create the window and set the coordinates
	win = GraphWin('Student Scores', 400, 200)
	win.setCoords(-10, -10, 100, 120)
	win.setBackground('white')

	# Draw in the names and rectangles
	for i in range(11):
		text = Text(Point(-5 + i * 10, -5), str(i))
		text.setSize(10)
		text.draw(win)
		height = count_list[i] * 100 / max(count_list)

		if count_list != 0:
			bar = Rectangle(Point(-7.5 + i * 10, 0), Point(-2.5 + i * 10, height))
			bar.draw(win)

	# Close the window and the file
	win.getMouse()
	win.close()
	infile.close()

main()


