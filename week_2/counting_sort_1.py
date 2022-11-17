# Complete the 'countingSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def countingSort(arr):
	min_element = min(arr)
	max_element = max(arr)

	# result = [0] * len(list(range(0, max_element + 1, 1)))
	result = [0] * 100
	for i in arr:
		result[i] += 1

	# result_sorted = []
	# for idx, val in enumerate(result):
	# 	if val > 0:
	# 		result_sorted += [idx] * val

	return result


if __name__ == '__main__':
	arr = [1, 1, 3, 2, 1]

	print(countingSort(arr))

