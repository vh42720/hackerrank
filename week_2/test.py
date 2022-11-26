# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

def flippingMatrix(matrix):
	n = len(matrix[0])
	max_sum = 0

	for i in range(int(n / 2)):
		for j in range(int(n / 2)):
			max_sum += max(matrix[i][j], matrix[i][n - j - 1], matrix[n - i - 1][j], matrix[n - i - 1][n - j - 1])

	return max_sum


if __name__ == '__main__':
	matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

	print(flippingMatrix(matrix))
