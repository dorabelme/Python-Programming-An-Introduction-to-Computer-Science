# Create nameless Student object with no credits or qpoints
# Get credits and grade for first class
# addGrade to student
# loop
	# prompt for number of credits for next class or Q
	# if Q
		# end loop
	# else
		# convert cred to float
		# get grade from user
		# addGrade to student
# print GPA

from student import Student

def main():
	student = Student("", 0, 0)
	cred = eval(input("Enter the number of credit hours for your first " +
						"class: "))
	grade = eval(input("Enter the grade you received for your first class: "))
	student.addGrade(grade, cred)

	while True:
		cred = input("Enter the number of credit hours for your next " +
						"class, Q to quit: ")
		if cred.isalpha():
			break
		else:
			cred = eval(cred)
			grade = eval(input("Enter the grade you received for your next " +
								"class: "))
			student.addGrade(grade, cred)

	print("\nGPA: {0}".format(student.gpa()))


main()

