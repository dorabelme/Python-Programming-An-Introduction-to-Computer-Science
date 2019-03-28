from student import Student

def main():
	student = Student("", 0, 0)
	cred = eval(input("Enter the number of credit hours for your first " +
						"class: "))
	grade = input("Enter the grade you received for your first class: ")
	if grade.isalpha():
		student.addLetterGrade(grade, cred)
	else:
		grade = eval(grade)
		student.addGrade(grade, cred)

	while True:
		cred = input("Enter the number of credit hours for your next " +
						"class, Q to quit: ")
		if cred.isalpha():
			break
		else:
			cred = eval(cred)
			grade = input("Enter the grade you received for your next " +
								"class: ")
			if grade.isalpha():
				student.addLetterGrade(grade, cred)
			else:
				grade = eval(grade)
				student.addGrade(grade, cred)

	print("\nGPA: {0}".format(student.gpa()))


main()

