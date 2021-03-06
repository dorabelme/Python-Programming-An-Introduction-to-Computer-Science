# gpasort.py
# A program to sort student information into GPA order.

from gpa import Student, makeStudent

# Get the name of the input file from the user
# Read student information into a list
# Sort the list by GPA
# Get the name of the output file from the user
# Write the student information from the list into a file

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
	print("This program sorts student grade information by GPA")
	filename = input("Enter then name of the data file: ")
	data = readStudents(filename)
	data.sort(key=Student.gpa)
	filename = input("Enter a name for the output file: ")
	writeStudents(data, filename)
	print("The data has been written to", filename)

if __name__ == '__main__':
	main()

	
