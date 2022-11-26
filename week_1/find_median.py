# Complete the 'findMedian' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def findMedian(arr):
	arr.sort()
	return arr[(len(arr) // 2)]

if __name__ == '__main__':
	arr = [5, 3, 1, 2, 4]

	print(findMedian(arr))
