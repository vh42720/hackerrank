# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.


def pickingNumbers(a):
	a.sort()

	current_array = []
	all_array = []

	for idx, val in enumerate(a):
		if idx == 0:
			current_array.append(val)
			continue

		if val - min(current_array) > 1:
			all_array.append(current_array)
			current_array = [val]
		else:
			current_array.append(val)

	all_array.append(current_array)

	return max([len(i) for i in all_array])


if __name__ == '__main__':
	a = [4, 6, 5, 3, 3, 1]
	print(pickingNumbers(a))
