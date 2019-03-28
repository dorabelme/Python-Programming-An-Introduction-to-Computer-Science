# create menu
# initialize win_count and loss_count to 0
# randomly choose a door
# get a choice from the user
# while the choice is not "Quit"
	# check if the choice is correct
	# update win_count and/or loss_count
	# display whether the user won or not
	# let user decide whether to play again or quit
	# if not "Quit"
		# randomly choose a door
		# get a choice from the user
# close the menu

from graphics import *
from random import randrange
from button import Button
from monte_menu import Menu

def main():
	menu = drawWin()

	win_count = 0
	loss_count = 0
	door = chooseDoor()
	choice = getChoice(menu)
	while choice != "Q":
		correct, win_count, loss_count = isCorrect(door, choice, win_count, 
																loss_count)
		quit_clicked = updateWin(menu, correct, win_count, loss_count)
		if not quit_clicked:
			door = chooseDoor()
			choice = getChoice(menu)
		else:
			choice = "Q"
	
	menu.close()

def drawWin():
	win = GraphWin("Three Door Monte", 400, 150)
	win.setCoords(0, 0, 12, 3)
	instr = Text(Point(6, 2.5), "Where's the car? Behind door number 1, \n" +
					"door number 2, or door number 3?")
	instr.setSize(10)
	instr.draw(win)
	win_loss_ctr = Text(Point(3, 0.5), "wins:	0\nlosses: 0")
	win_loss_ctr.setSize(10)
	win_loss_ctr.setFace("courier")
	win_loss_ctr.draw(win)

	btn1 = Button(win, Point(2, 1.5), 2, 0.75, "Door 1")
	btn2 = Button(win, Point(6, 1.5), 2, 0.75, "Door 2")
	btn3 = Button(win, Point(10, 1.5), 2, 0.75, "Door 3")
	qbtn = Button(win, Point(10, 0.5), 2, 0.75, "Quit")
	menu = Menu(win, instr, win_loss_ctr, btn1, btn2, btn3, qbtn)
	return menu

def chooseDoor():
	winning_door = randrange(1, 4)
	return winning_door

def getChoice(menu):
	pt = menu.getMouse()
	while not menu.button_clicked(pt):
		pt = menu.getMouse()
	if menu.btn1_clicked(pt):
		return 1
	elif menu.btn2_clicked(pt):
		return 2
	elif menu.btn3_clicked(pt):
		return 3
	else: 
		return "Q"

def isCorrect(door, choice, win_count, loss_count):
	if choice == door:
		return True, win_count + 1, loss_count
	else:
		return False, win_count, loss_count + 1

def updateWin(menu, correct, win_count, loss_count):
	menu.deactivate_btns()
	if correct:
		menu.setPrompt("You've won the car!\nClick anywhere to play again.")
	else:
		menu.setPrompt("Sorry, You've chosen the goat.\nClick anywhere to play again.")
	menu.setCounter("wins: {0:3d}\nlosses: {1}".format(win_count, loss_count))
	pt = menu.getMouse()
	if not menu.quit_clicked(pt):
		menu.setPrompt("Where's the car? Behind door number 1,\n" +
				"door number 2, or door number 3?")
		menu.activate_btns()
	return menu.quit_clicked(pt)

main()


