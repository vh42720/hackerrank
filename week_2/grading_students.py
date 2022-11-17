# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grades):
	ret_grade = []
	for grade in grades:
		if grade < 38:
			ret_grade.append(grade)
		elif grade % 5 in (3, 4):
			ret_grade.append((grade // 5 + 1) * 5)
		else:
			ret_grade.append(grade)

	return ret_grade


if __name__ == '__main__':
	grades = [84, 29, 57]

	print(gradingStudents(grades))
