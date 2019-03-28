# textpoker.py == video dice poker using a text-based interface

from random import randrange
from graphics import *
from chapter12_button import Button
from chapter12_dieview2 import DieView 
from chapter12_dice import Dice


class PokerApp:

	def __init__(self, interface):
		self.dice = Dice()
		self.money = 100
		self.interface = interface

	def run(self):
		while self.money >= 10 and self.interface.wantToPlay():
			self.playRound()
		self.interface.close()

	def playRound(self):
		self.money = self.money - 10
		self.interface.setMoney(self.money)
		self.doRolls()
		result, score = self.dice.score()
		self.interface.showResult(result, score)
		self.money = self.money + score
		self.interface.setMoney(self.money)

	def doRolls(self):
		self.dice.rollAll()
		roll = 1
		self.interface.setDice(self.dice.values())
		toRoll = self.interface.chooseDice()
		while roll < 3 and toRoll != []:
			self.dice.roll(toRoll)
			roll = roll + 1
			self.interface.setDice(self.dice.values())
			if roll < 3:
				toRoll = self.interface.chooseDice()

class TextInterface:

	def __init__(self):
		print("Welcome to video poker.")

	def setMoney(self, amt):
		print("You currently have ${0}.".format(amt))

	def setDice(self, values):
		print("Dice:", values)

	def wantToPlay(self):
		ans = input("Do you wish to try your luck? ")
		return ans[0] in "yY"

	def close(self):
		print("\nThanks for playing!")

	def showResult(self, msg, score):
		print("{0}. You win ${1}.".format(msg, score))

	def chooseDice(self):
		return eval(input("Enter list of which to change ([] to stop) "))

class GraphicsInterface:

	def __init__(self):
		self.win = GraphWin("Dice Poker", 600, 400)
		self.win.setBackground("green3")

		banner = Text(Point(300, 30), "Python Poker Parlor")
		banner.setSize(24)
		banner.setFill("yellow2")
		banner.setStyle("bold")
		banner.draw(self.win)

		self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
		self.msg.setSize(18)
		self.msg.draw(self.win)

		self.createDice(Point(300,100), 75)
		self.buttons = []
		self.addDiceButtons(Point(300,170), 75, 30)
		b = Button(self.win, Point(300,230), 400, 40, "Roll Dice")
		self.buttons.append(b)
		b = Button(self.win, Point(300, 280), 150, 40, "Score")
		self.buttons.append(b)
		b = Button(self.win, Point(570,375), 40, 30, "Quit")
		self.buttons.append(b)

		self.money = Text(Point(300,325), "$100")
		self.money.setSize(18)
		self.money.draw(self.win)

	def createDice(self, center, size):
		center.move(-3 * size, 0)
		self.dice = []
		for i in range(5):
			view = DieView(self.win, center, size)
			self.dice.append(view)
			center.move(1.5 * size, 0)

	def addDiceButtons(self, center, width, height):
		center.move(-3 * width, 0)
		for i in range(1, 6):
			label = "Die {0}".format(i)
			b = Button(self.win, center, width, height, label)
			self.buttons.append(b)
			center.move(1.5 * width, 0)

	def setMoney(self, amt):
		self.money.setText("${0}".format(amt))

	def showResult(self, msg, score):
		if score > 0:
			text = "{0}! You win ${1}".format(msg, score)
		else:
			text = "You rolled {0}".format(msg)
		self.msg.setText(text)

	def setDice(self, values):
		for i in range(5):
			self.dice[i].setValue(values[i])

	def wantToPlay(self):
		ans = self.choose(["Roll Dice", "Quit"])
		self.msg.setText("")
		return ans

	def chooseDice(self):
		# choices is a list of the indexes of the selected dice
		choices = []				# No dice chosen yet
		while True:
			# wait for user to click a valid button
			b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
								"Roll Dice", "Score"])

			if b[0] == "D":				# User clicked a die button
				i = int(b[4]) - 1		# Translate label to die index
				if i in choices:		# Currently selected, unselect it
					choices.remove[i]
					self.dice[i].setColor("black")
				else:					# Currently deselected, select it
					choices.append(i)
					self.dice[i].setColor("gray")
			else:						# User clicked Roll or Score
				for d in self.dice:		# Revert appearance of all dice
					d.setColor("black")
				if b == "Score":		# Score clicked, ignore choices
					return []
				elif choices != []:		# Don't accept Roll unless some
					return choices		# dice are actually selected

	def choose(self, choices):
		buttons = self.buttons

		# activate choice buttons, deactivate others
		for b in buttons:
			of b.getLabel() in choices:
			b.activate()

		# get mouse clicks until an active button is clicked
		while True:
			p = self.win.getMouse()
			for b in buttons:
				if b.clicked(p):
					return b.getLabel()

	def close(self):
		self.win.close()

inter = GraphicsInterface()
app = PokerApp(inter)
app.run()


