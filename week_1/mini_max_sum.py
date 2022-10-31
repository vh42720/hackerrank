# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
	arr.sort()

	print(sum(arr[:4]), sum(arr[-4:]))


if __name__ == '__main__':
	arr = [1, 3, 5, 7, 9]

	miniMaxSum(arr)
