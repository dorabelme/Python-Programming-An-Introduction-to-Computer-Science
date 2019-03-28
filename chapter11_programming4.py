# Give the program from the previous exercise(s) a graphical interface.
# You should have Entrys for the input and output file name and a button for
# each sorting order.

from chapter10_gpa import Student, makeStudent
from graphics import *
from chapter10_button import Button

def readStudents(filename):
	infile = open(filename, "r")
	students = []
	for line in infile:
		students.append(makeStudent(line))
	infile.close()
	return students

def writeStudents(students, filename):
	# students is a list of Student objects
	outfile = open(filename, "w")
	for s in students:
		print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),
				file=outfile)
	outfile.close()

def main():
	# Create window and Entry objects
	win = GraphWin('Data Sorting', 400, 200)
	inputText = Text(Point(95,40), "Enter the name of the data file")
	inputText.draw(win)
	inputFileName = Entry(Point(280,40), 30)
	inputFileName.draw(win)
	outputText = Text(Point(95, 70), "Enter the name of the output file")
	outputText.draw(win)
	outfileName = Entry(Point(280,70), 30)
	outfileName.draw(win)

	# Introduction
	messageText = Text(Point(200,10), "This program sorts student data from one file " +
										"and outputs it to another file.")
	messageText.draw(win)

	# Create buttons
	GPAsort = Button(win, Point(60,130), 80, 20, "Sort by GPA")
	Namesort = Button(win, Point(180, 130), 80, 20, "Sort by Name")
	Creditssort = Button(win, Point(300,130), 80, 20, "Sort by Credits")
	ascendingButton = Button(win, Point(120,160), 100, 20, "Ascending Order")
	descendingButton = Button(win, Point(260,160), 100, 20, "Descending Order")
	quitButton = Button(win, Point(370,180), 50, 20, "Quit")
	enterButton = Button(win, Point(300,100), 120,20, "Submit file info")
	sortButton = Button(win, Point(100,100), 80, 20, "Sort Data")

	# while user has not chosen to quit the program
	enterButton.activate()
	p = win.getMouse()
	while not quitButton.clicked(p):

		# obtain dta to sort and file to output to
		filename = inputFileName.getText()
		data = readStudents(filename)
		filename2 = outfileName.getText()
		enterButton.deactivate()
		quitButton.deactivate()

		# user chooses a sorting method
		messageText.setText("Please click a button to sort by either GPA, name, or credit hours")
		GPAsort.activate()
		Namesort.activate()
		Creditssort.activate()
		p = win.getMouse()
		if GPAsort.clicked(p):
			key = Student.gpa
		elif Namesort.clicked(p):
			key = Student.getName
		else:
			key = Student.getHours

		GPAsort.deactivate()
		Namesort.deactivate()
		Creditssort.deactivate()

		# user chooses to sort by ascending or descending order
		messageText.setText("Please click a button to choose to sort in ascending or descending order.")
		ascendingButton.activate()
		descendingButton.activate()
		p = win.getMouse()
		if descendingButton.clicked(p):
			reverse = True
		else:
			reverse = False
		ascendingButton.deactivate()
		descendingButton.deactivate()

		# sort data and output to file
		messageText.setText("Click the sort button to sort the data.")
		sortButton.activate()
		win.getMouse()
		data.sort(key=key, reverse=reverse)
		writeStudents(data, filename)
		sortButton.deactivate()

		# allow user to enter another file
		enterButton.activate()
		quitButton.activate()
		messageText.setText('Enter another file or click quit to exit.')
		p = win.getMouse()

	# close window
	win.close()


if __name__ == '__main__':
	main()


