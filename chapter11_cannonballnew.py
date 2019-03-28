from chapter10_shottracker import ShotTracker 
from graphics import *
from math import *

class Launcher:

	def __init__(self, win):
		# draw the base shot of the launcher
		base = Circle(Point(0,0), 3)
		base.setFill("red")
		base.setOutline("red")
		base.draw(win)

		# save the window and create initial angle and velocity
		self.win = win
		self.angle = radians(45.0)
		self.vel = 40.0

		# create initial "dummy" arrow (needed by redraw)
		self.arrow = Line(Point(0,0), Point(0,0)).draw(win)
		# replace it with the correct arrow
		self.redraw()

	def adjAngle(self,amt):
		"""Changes launch angle by amt degrees"""
		self.angle = self.angle + radians(amt)
		self.redraw()

	def adjVel(self, amt):
		"""change launch velocity by amt"""
		self.vel = self.vel + amt
		self.redraw()

	def redraw(self):
		"""redraw the arrow to show current angle and velocity"""
		self.arrow.undraw()
		pt2 = Point(self.vel*cos(self.angle),
					self.vel*sin(self.angle))
		self.arrow = Line(Point(0,0), pt2).draw(self.win)
		self.arrow.setArrow("last")
		self.arrow.setWidth(3)

	def fire(self):
		return ShotTracker(self.win, degrees(self.angle), self.vel, 0.0)


class ProjectileApp:

	def __init__(self):
		# create graphics windown with a scale line at the bottom
		self.win = GraphWin("Projectile Animation", 640, 480)
		self.win.setCoords(-10, -10, 210, 155)
		Line(Point(-10, 0), Point(210, 0)).draw(self.win)
		for x in range(0, 210, 50):
			Text(Point(x, -7), str(x)).draw(self.win)
			Line(Point(x, 0), Point(x, 2)).draw(self.win)

		# add the launcher to the window
		self.launcher = Launcher(self.win)

		# starts with an empty list of "live" shots
		self.shots = []

	def updateShots(self, dt):
		for shot in self.shots:
			shot.update(dt)

		alive = []
		for shot in self.shots:
			shot.update(dt)
			if shot.getY() >= 0 and -10 < shot.getX() < 210:
				alive.append(shot)
			else:
				shot.undraw()
		self.shots = alive

	def run(self):
		# main event / animation loop
		while True:
			self.updateShots(1/30)

			key = self.win.checkKey()
			if key in ["q", "Q"]:
				break

			if key == "Up":
				self.launcher.adjAngle(5)
			elif key == "Down":
				self.launcher.adjAngle(-5)
			elif key == "Right":
				self.launcher.adjVel(5)
			elif key == "Left":
				self.launcher.adjVel(-5)
			elif key in ["f", "F"]:
				self.shots.append(launcher.fire())

			update(30)

		win.close()

if __name__ == '__main__':
	ProjectileApp().run()



