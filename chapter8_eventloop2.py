# event_loop2.py 

from graphics import *

def handleKey(k, win):
	if key == "r":
		win.setBackground("pink")
	elif key == "w":
		win.setBackground("white")
	elif key == "g":
		win.setBackground("lightgray")
	elif key == "b":
		win.setBackground("lightblue")

def handleClick(pt, win):
	# create an Entry for user to type is
	entry = Entry(pt, 10)
	entry.draw(win)

	# Go modal: loop until user types <Enter> key
	while True:
		key = win.getKey()
		if key == "Return": break

	# Undraw the entry and create and draw Text()
	entry.undraw()
	typed = entry.getText()
	Text(pt, typed).draw(win)

	win.checkMouse()

def main():
	win = GraphWin("Click and Type", 500,500)

	# Event Loop: handle key presses and mouse clicks until user
	# presses the "q" key
	while True:
		key = win.checkKey()
		if key == "q":
			break		# loop exit
		
		if key:
			handleKey(key, win)

		pt = win.checkMouse()
		if pt:
			handleClick(pt, win)

	win.close()

main()


