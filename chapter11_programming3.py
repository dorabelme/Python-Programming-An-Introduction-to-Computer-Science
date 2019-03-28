# gpasort.py
# A program to sort student information into GPA order.

from gpa import Student, makeStudent

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
	sort_type = input("Would you like to sort by 'gpa', 'name', or 'credits'? ")
	while sort_type not in ['gpa', 'name', 'credits']:
		print("Invalid choice")
		sort_type = input("Would you like to sort by 'gpa', 'name', or 'credits'? ")

	asc_or_desc = input("'Ascending' or 'descending' order? ")
	is_descending = asc_or_desc.lower() == 'descending'

	data = readStudents(filename)
	if sort_type == 'gpa':
		data.sort(key=Student.gpa, reverse=is_descending)
	elif sort_type == 'name':
		data.sort(key=Student.getName, reverse=is_descending)
	else:
		data.sort(key=Student.getHours, reverse=is_descending)
	
	filename = input("Enter a name for the output file: ")
	writeStudents(data, filename)
	print("The data has been written to", filename)

if __name__ == '__main__':
	main()

	
