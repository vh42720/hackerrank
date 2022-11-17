# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):
	n = len(arr)
	idx = list(range(n))

	primary_sum = 0
	secondary_sum = 0

	for ar, i in zip(arr, idx):
		primary_sum += ar[i]
		secondary_sum += ar[n - i - 1]

	return abs(primary_sum - secondary_sum)


if __name__ == '__main__':
	arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
	print(diagonalDifference(arr))
