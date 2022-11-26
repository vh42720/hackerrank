# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def minimumAbsoluteDifference(arr):
	arr.sort()
	return min([abs(i - j) for i, j in zip(arr[:-1], arr[1:])])


if __name__ == '__main__':
	arr = [-2, 2, 4]

	print(minimumAbsoluteDifference(arr))
