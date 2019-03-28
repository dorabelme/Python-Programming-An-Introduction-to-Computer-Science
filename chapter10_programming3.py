# create the menu window
# choose a door number
# get a choice from the user
# determine if the user won
# display the result
# close the window after another mouse click

from graphics import *
from random import randrange
from button import Button
from monte_menu import Menu

def main():
	menu = drawWin()
	door = chooseDoor()
	choice = getChoice(menu)
	correct = isCorrect(door, choice)
	updateWin(menu, correct)

	menu.getMouse()
	menu.close()

def drawWin():
	win = GraphWin("Three Door Monte", 400, 100)
	win.setCoords(0, 0, 12, 2)
	instr = Text(Point(6, 1.5), "Where's the car? Behind door number 1, \n" +
					"door number 2, or door number 3?")
	instr.setSize(10)
	instr.draw(win)
	btn1 = Button(win, Point(2, 0.5), 2, 0.75, "Door 1")
	btn1.activate()
	btn2 = Button(win, Point(6, 0.5), 2, 0.75, "Door 2")
	btn2.activate()
	btn3 = Button(win, Point(10, 0.5), 2, 0.75, "Door 3")
	btn3.activate()
	menu = Menu(win, instr, btn1, btn2, btn3)
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
	else: 
		return 3

def isCorrect(door, choice):
	if choice == door:
		return True
	else:
		return False

def updateWin(menu, correct):
	menu.deactivate_btns()
	if correct:
		menu.setPrompt("You've won the car!")
	else:
		menu.setPrompt("Sorry, You've chosen the goat.")

main()

