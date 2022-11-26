# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.


def closestNumbers(arr):
	arr.sort()
	min_dis = abs(arr[1] - arr[0])
	pair_list = []

	for idx, val in enumerate(arr):
		if idx + 1 >= len(arr):
			break

		if (temp_dis := abs(val - arr[idx + 1])) == min_dis:
			min_dis = temp_dis
			pair_list += [val, arr[idx + 1]]
		elif temp_dis < min_dis:
			min_dis = temp_dis
			pair_list = [val, arr[idx + 1]]

	return pair_list


if __name__ == '__main__':
	# arr = [5, 2, 3, 4, 1]
	arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
	print(closestNumbers(arr))
