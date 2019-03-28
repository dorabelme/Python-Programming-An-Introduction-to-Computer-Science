class Student():

	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)

	def getName(self):
		return self.name

	def getHours(self):
		return self.hours

	def getQPoints(self):
		return self.qpoints

	def gpa(self):
		return self.qpoints / self.hours

	def addGrade(self, gradePoint, credits):
		self.qpoints += gradePoint * credits
		self.hours += credits

	def addLetterGrade(self, letterGrade, credits):
		if letterGrade[0] == 'A':
			gradePoint = 4
		elif letterGrade[0] == 'B':
			gradePoint = 3
		elif letterGrade[0] =='C':
			gradePoint = 2
		elif letterGrade[0] == 'D':
			gradePoint = 1
		else:
			gradePoint = 0
		if len(letterGrade) == 2:
			if letterGrade[1] == "+" and letterGrade[0] != A:
				gradePoint += 0.3
			elif letterGrade[1] == "-":
				gradePoint -= 0.3
		self.addGrade(gradePoint, credits)
		