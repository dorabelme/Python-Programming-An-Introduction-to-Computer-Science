class Menu:

	def __init__(self, win, prompt, counter, btn1, btn2, btn3, qbtn):
		self.win = win
		self.prompt = prompt
		self.ctr = counter
		self.btn1 = btn1
		self.btn1.activate()
		self.btn2 = btn2
		self.btn2.activate()
		self.btn3 = btn3
		self.btn3.activate()
		self.quit = qbtn
		self.quit.activate()

	def setPrompt(self, text):
		self.prompt.setText(text)

	def setCounter(self, text):
		self.ctr.setText(text)

	def btn1_clicked(self, pt):
		return self.btn1.clicked(pt)

	def btn2_clicked(self, pt):
		return self.btn2.clicked(pt)

	def btn3_clicked(self, pt):
		return self.btn3.clicked(pt)

	def quit_clicked(self, pt):
		return self.quit.clicked(pt)

	def button_clicked(self, pt):
		return (self.btn1.clicked(pt) or self.btn2.clicked(pt) or 
			self.btn3.clicked(pt))

	def deactivate_btns(self):
		self.btn1.deactivate()
		self.btn2.deactivate()
		self.btn3.deactivate()

	def activate_btns(self):
		self.btn1.activate()
		self.btn2.activate()
		self.btn3.activate()

	def getMouse(self):
		return self.win.getMouse()

	def close(self):
		self.win.close()


		